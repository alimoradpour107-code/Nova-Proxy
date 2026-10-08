import reflex as rx

config = rx.Config(
    app_name="app",
    app_module_import="app.app",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
