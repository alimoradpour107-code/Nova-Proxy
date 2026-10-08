import reflex as rx


def documentation_link(
    title: str, description: str, href: str, icon: str
) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="h-5 w-5 shrink-0 text-cyan-300"),
        rx.el.div(
            rx.el.h3(title, class_name="text-sm font-semibold text-slate-100"),
            rx.el.p(
                description, class_name="mt-1 text-sm leading-6 text-slate-400"
            ),
            class_name="flex-1",
        ),
        rx.icon("arrow-up-right", class_name="h-4 w-4 shrink-0 text-slate-400"),
        href=href,
        target="_blank",
        rel="noopener noreferrer",
        class_name="flex items-start gap-4 rounded-xl border border-slate-800 bg-slate-900/60 p-5 transition-colors hover:border-cyan-300/40 hover:bg-slate-900 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-cyan-300",
    )


def project_link(label: str, href: str, icon: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="h-4 w-4 text-slate-400"),
        label,
        rx.icon("arrow-up-right", class_name="h-3 w-3 text-slate-500"),
        href=href,
        target="_blank",
        rel="noopener noreferrer",
        class_name="flex items-center gap-2 text-sm text-slate-300 transition-colors hover:text-cyan-300 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-cyan-300",
    )


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.header(
                rx.el.a(
                    rx.icon("orbit", class_name="h-7 w-7 text-cyan-300"),
                    rx.el.span(
                        "Nova Proxy",
                        class_name="text-lg font-semibold tracking-tight text-slate-100",
                    ),
                    href="/",
                    class_name="flex items-center gap-3 focus-visible:outline-2 focus-visible:outline-cyan-300",
                ),
                rx.el.span(
                    "PROJECT GUIDE",
                    class_name="rounded-md border border-slate-800 bg-slate-900 px-3 py-1.5 text-[10px] font-medium tracking-[0.15em] text-slate-400",
                ),
                class_name="flex items-center justify-between gap-4 border-b border-slate-800 pb-6",
            ),
            rx.el.section(
                rx.el.p(
                    "SELF-HOSTED · CLOUDFLARE WORKERS",
                    class_name="text-xs font-medium tracking-[0.14em] text-cyan-300",
                ),
                rx.el.h1(
                    "Your proxy. Your Cloudflare account.",
                    class_name="mt-5 max-w-xl text-4xl font-semibold leading-tight tracking-tight text-slate-100 sm:text-5xl",
                ),
                rx.el.p(
                    "Nova Proxy is a self-hosted proxy project with a multilingual admin panel. Explore the project documentation to learn about its features, deployment, and updates.",
                    class_name="mt-5 max-w-xl text-base leading-7 text-slate-400",
                ),
                class_name="py-10 sm:py-12",
            ),
            rx.el.aside(
                rx.icon(
                    "info", class_name="mt-0.5 h-5 w-5 shrink-0 text-cyan-300"
                ),
                rx.el.div(
                    rx.el.h2(
                        "Documentation preview only",
                        class_name="text-sm font-semibold text-slate-100",
                    ),
                    rx.el.p(
                        "The actual proxy and admin panel run on Cloudflare Workers, not in this Reflex preview. This page does not proxy traffic or provide admin controls. Follow the deployment guide to run Nova in your own Cloudflare account.",
                        class_name="mt-2 text-sm leading-6 text-slate-400",
                    ),
                ),
                class_name="flex gap-3 rounded-xl border border-cyan-300/20 bg-slate-900/60 p-5",
            ),
            rx.el.section(
                rx.el.h2(
                    "Start with the documentation",
                    class_name="mb-4 text-base font-semibold text-slate-100",
                ),
                rx.el.div(
                    documentation_link(
                        "README",
                        "Project overview, features, and getting started.",
                        "https://github.com/IRNova/Nova-Proxy/blob/main/README.md",
                        "book-open",
                    ),
                    documentation_link(
                        "Deployment guide",
                        "Installation, release verification, updates, and rollback.",
                        "https://github.com/IRNova/Nova-Proxy/blob/main/DEPLOY.md",
                        "file-text",
                    ),
                    class_name="grid grid-cols-1 gap-3 sm:grid-cols-2",
                ),
                class_name="mt-8",
            ),
            rx.el.section(
                rx.el.h2(
                    "Official project links",
                    class_name="mb-4 text-base font-semibold text-slate-100",
                ),
                rx.el.nav(
                    project_link(
                        "GitHub repository",
                        "https://github.com/IRNova/Nova-Proxy",
                        "code",
                    ),
                    project_link(
                        "Project website", "https://novaproxy.online/", "globe"
                    ),
                    project_link(
                        "Telegram channel", "https://t.me/irnova_proxy", "send"
                    ),
                    aria_label="Official project links",
                    class_name="flex flex-wrap gap-x-6 gap-y-4",
                ),
                class_name="mt-8",
            ),
            rx.el.footer(
                rx.el.p(
                    "Nova Proxy · Informational preview",
                    class_name="text-xs text-slate-500",
                ),
                rx.el.a(
                    "فارسی README",
                    href="https://github.com/IRNova/Nova-Proxy/blob/main/README.fa.md",
                    target="_blank",
                    rel="noopener noreferrer",
                    lang="fa",
                    class_name="text-xs text-slate-400 hover:text-cyan-300 focus-visible:outline-2 focus-visible:outline-cyan-300",
                ),
                class_name="mt-10 flex flex-wrap items-center justify-between gap-4 border-t border-slate-800 pt-5",
            ),
            class_name="mx-auto w-full max-w-3xl px-6 py-8 sm:px-10 sm:py-12",
        ),
        class_name="min-h-dvh w-full bg-[#080f1e] font-sans text-slate-100 selection:bg-cyan-300/20",
    )


app = rx.App(theme=rx.theme(appearance="light"))
app.add_page(
    index,
    route="/",
    title="Nova Proxy | Project Guide",
    description="An informational preview for Nova Proxy. Read the project and deployment guides for the actual Cloudflare Workers proxy and admin panel.",
)
