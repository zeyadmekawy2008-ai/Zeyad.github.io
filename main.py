import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Zeyad Quran"
    page.theme_mode = ft.ThemeMode.DARK
    page.rtl = True
    page.bgcolor = "#0f172a"
    page.scroll = "auto"

    def get_surahs():
        try:
            response = requests.get("https://api.alquran.cloud/v1/surah")
            return response.json()['data']
        except: return None

    page.add(ft.Text("السلام عليكم مع Zeyad quran", size=25, color="#fbbf24", weight="bold"))
    
    surahs = get_surahs()
    if surahs:
        for surah in surahs:
            page.add(ft.ListTile(title=ft.Text(surah['name']), leading=ft.Icon(ft.icons.PLAY_CIRCLE_FILL)))

# السطر ده هو اللي هيشغل الموقع ويب بدون خطأ 404
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
