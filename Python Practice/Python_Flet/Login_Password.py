import flet as ft
import sqlite3


def main(page: ft.Page):
    page.title = 'Login-Password'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 400
    page.window_resizable = False


    def register(e):
      db = sqlite3.connect('DB_for_Login_Password')

      cur = db.cursor()
      cur.execute("""CREATE TABLE IF NOT EXISTS users(
                  ID INTEGER PRIMARY KEY,
                  login TEXT,
                  password TEXT
      )""")

      cur.execute(f"INSERT INTO users VALUES(NULL, '{user_login.value}', '{user_pass.value}')")
      print(cur.fetchone())

      db.commit()
      db.close()

      user_login.value = ''
      user_pass.value = ''
      btn_reg.text = 'Добавлено'

      page.update()

    def auth_user(e):
      db = sqlite3.connect('DB_for_Login_Password')

      cur = db.cursor()

      cur.execute(f"SELECT * FROM users WHERE login = '{user_login.value}' AND password = '{user_pass.value}'")

      if cur.fetchone() != None:
        user_login.value = ''
        user_pass.value = ''
        btn_auth.text = 'Авторизовано'

        if len(page.navigation_bar.destinations) == 2:

          page.navigation_bar.destinations.append(ft.NavigationDestination(
              icon = ft.icons.BOOK,
              label='Кабинет',
              selected_icon=ft.icons.BOOKMARK
          ))

        page.update()
      else:
        page.snack_bar = ft.SnackBar(ft.Text('Неверно введенные данные'))
        page.snack_bar.open = True
        page.update()

      db.commit()
      db.close()


    def validate(e):
      if all([user_login.value, user_pass.value]):
        btn_reg.disabled = False
        btn_auth.disabled = False
      else:
        btn_reg.disabled = True
        btn_auth.disabled = True
      page.update()

    user_login = ft.TextField(label='Логин', width=200, on_change=validate)
    user_pass = ft.TextField(label='Пароль', password=True, width=200, on_change=validate)
    btn_reg = ft.OutlinedButton(text='Добавить', width=200, on_click=register, disabled=True)
    btn_auth = ft.OutlinedButton(text='Войти', width=200, on_click=auth_user, disabled=True)

    # user_cabinet

    user_list = ft.ListView(spacing=10, padding = 20)

    # user_cabinet_end


    panel_register = ft.Row(
        [
          ft.Column(
            [
              ft.Text('Регистрация'),
              user_login,
              user_pass,
              btn_reg
            ]
          )
        ],
        alignment=ft.MainAxisAlignment.CENTER
      )

    panel_auth = ft.Row(
        [
          ft.Column(
            [
              ft.Text('Авторизация'),
              user_login,
              user_pass,
              btn_auth
            ]
          )
        ],
        alignment=ft.MainAxisAlignment.CENTER
      )

    panel_kabinet = ft.Row(
        [
          ft.Column(
            [
              ft.Text('Личный кабинет'),
              user_list
            ]
          )
        ],
        alignment=ft.MainAxisAlignment.CENTER
      )

    def navigate(e):
      index = page.navigation_bar.selected_index
      page.clean()

      if index == 0: page.add(panel_register)
      elif index == 1: page.add(panel_auth)
      elif index == 2: 
            user_list.controls.clear()

            db = sqlite3.connect('DB_for_Login_Password')
            cur = db.cursor()
            cur.execute('SELECT * FROM users')
            res = cur.fetchall()

            if res != None:
              for user in res:
                print(user)
                user_list.controls.append(ft.Row([
                    ft.Text(f'User {user[1]}'),
                    ft.Icon(ft.icons.VERIFIED_USER_ROUNDED)
                ]))

            db.commit()
            db.close()
        
            page.add(panel_kabinet)

    page.navigation_bar = ft.NavigationBar(
      destinations=[
        ft.NavigationDestination(icon=ft.icons.VERIFIED_USER, label='Регистрация'),
        ft.NavigationDestination(icon=ft.icons.VERIFIED_USER_OUTLINED, label='Авторизация')
      ], on_change=navigate
    )

    page.add(panel_register)

ft.app(target=main) # - для пк приложения
# ft.app(target=main, view=ft.AppView.WEB_BROWSER) # - для веб приложения