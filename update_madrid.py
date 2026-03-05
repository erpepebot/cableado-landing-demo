#!/usr/bin/env python3
"""Create Madrid-optimized variants of the 3 demo landings.

Produces:
- v1-dark-madrid.html
- v2-light-madrid.html
- v3-industrial-madrid.html

Edits are conservative: keep layout/styles, replace copy + CTAs, and connect a placeholder Odoo form endpoint.
"""

from __future__ import annotations

from pathlib import Path

ODOO_PLACEHOLDER = "https://odoo.impulsotecnologico.com/website/form/cableado_madrid"  # placeholder only
PHONE_DISPLAY = "91 505 7575"
PHONE_TEL = "+34915057575"

META_TITLE_DEFAULT = "Cableado de redes informáticas en Madrid | Instalación y certificación"
META_DESC_DEFAULT = (
    "Instalación de cableado de redes informáticas en Madrid (Cat6/Cat6A/fibra), racks y WiFi. "
    "Etiquetado, pruebas y documentación. Respuesta en 24h."
)


def replace_all(content: str, pairs: list[tuple[str, str]]) -> str:
    for old, new in pairs:
        if old in content:
            content = content.replace(old, new)
    return content


def transform_v1(content: str) -> str:
    pairs = [
        (
            "<title>Cableado de Redes | Instalación profesional (Cat6/Cat6A/Fibra)</title>",
            f"<title>{META_TITLE_DEFAULT}</title>",
        ),
        (
            "<meta name=\"description\" content=\"Servicio profesional de cableado estructurado: diseño, instalación y certificación. Cat6/Cat6A, racks, patch panels, WiFi y electrónica de red.\" />",
            f"<meta name=\"description\" content=\"{META_DESC_DEFAULT}\" />",
        ),
        (
            "Instalación + certificación · Entrega rápida",
            "Instalación + pruebas · Madrid y alrededores",
        ),
        (
            "Cableado de redes <span class=\"text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-cyan-300\">profesional</span>\n          para oficinas, naves y comercios",
            "Cableado de <span class=\"text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-cyan-300\">redes informáticas</span>\n          en Madrid (Cat6/Cat6A y fibra)",
        ),
        (
            "Diseñamos e instalamos cableado estructurado (Cat6/Cat6A/fibra), racks, patch panels y WiFi.\n          Documentación, etiquetado y certificación para que tu red sea estable y escalable.",
            "Diseñamos e instalamos <strong>cableado de redes informáticas</strong> para empresas y centros de trabajo en <strong>Madrid</strong>: "
            "puntos RJ45 (Cat6/Cat6A), fibra (si aplica), racks, patch panels y WiFi.\n          "
            "Incluye <strong>pruebas</strong>, <strong>etiquetado</strong> y <strong>documentación</strong> (mapa de puntos + checklist) "
            "para una red estable y escalable.",
        ),
        (
            ">Solicitar visita técnica</a>",
            ">Solicitar presupuesto</a>",
        ),
        (
            "<h2 class=\"text-3xl font-extrabold tracking-tight\">¿Te hacemos una propuesta hoy?</h2>",
            "<h2 class=\"text-3xl font-extrabold tracking-tight\">Solicita presupuesto en Madrid</h2>",
        ),
        (
            "Cuéntanos nº de puestos y si hay canalización. Te respondemos con rango y siguientes pasos.",
            "Cuéntanos el nº de puestos, si ya hay canalización y el tipo de espacio. Te respondemos con un rango orientativo y los siguientes pasos.",
        ),
        (
            "<form class=\"rounded-2xl border border-white/10 bg-slate-950/30 p-6\">",
            f"<form method=\"post\" action=\"{ODOO_PLACEHOLDER}\" class=\"rounded-2xl border border-white/10 bg-slate-950/30 p-6\">",
        ),
        (
            "<div><label class=\"text-xs text-slate-400\">Nombre</label><input class=\"mt-1 w-full rounded-xl border border-white/10 bg-slate-950/40 px-4 py-2 text-sm text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"Tu nombre\" /></div>\n            <div><label class=\"text-xs text-slate-400\">Email o teléfono</label><input class=\"mt-1 w-full rounded-xl border border-white/10 bg-slate-950/40 px-4 py-2 text-sm text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"nombre@empresa.com\" /></div>\n            <div><label class=\"text-xs text-slate-400\">Qué necesitas</label><textarea rows=\"4\" class=\"mt-1 w-full rounded-xl border border-white/10 bg-slate-950/40 px-4 py-2 text-sm text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"Ej.: 20 puestos, rack 12U, 2 APs PoE, Cat6A...\"></textarea></div>",
            "<div><label class=\"text-xs text-slate-400\">Nombre y apellidos</label><input name=\"name\" required autocomplete=\"name\" class=\"mt-1 w-full rounded-xl border border-white/10 bg-slate-950/40 px-4 py-2 text-sm text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"Tu nombre\" /></div>\n            "
            "<div><label class=\"text-xs text-slate-400\">Teléfono</label><input name=\"phone\" required autocomplete=\"tel\" class=\"mt-1 w-full rounded-xl border border-white/10 bg-slate-950/40 px-4 py-2 text-sm text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"+34 ...\" /></div>\n            "
            "<div><label class=\"text-xs text-slate-400\">Email</label><input name=\"email_from\" type=\"email\" required autocomplete=\"email\" class=\"mt-1 w-full rounded-xl border border-white/10 bg-slate-950/40 px-4 py-2 text-sm text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"tu@empresa.com\" /></div>\n            "
            "<div><label class=\"text-xs text-slate-400\">Mensaje</label><textarea name=\"description\" rows=\"4\" required class=\"mt-1 w-full rounded-xl border border-white/10 bg-slate-950/40 px-4 py-2 text-sm text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"Ej.: 20 puestos, canaleta existente, rack 12U, 2 APs PoE, Cat6A...\"></textarea></div>\n            "
            "<input type=\"hidden\" name=\"x_service\" value=\"Cableado de redes informáticas\" />\n            "
            "<input type=\"hidden\" name=\"x_city\" value=\"Madrid\" />",
        ),
        (
            "<button type=\"button\" class=\"inline-flex w-full items-center justify-center rounded-xl bg-brand-500 px-5 py-3 text-sm font-semibold text-white hover:bg-brand-400\">Enviar (demo)</button>",
            "<button type=\"submit\" class=\"inline-flex w-full items-center justify-center rounded-xl bg-brand-500 px-5 py-3 text-sm font-semibold text-white hover:bg-brand-400\">Solicitar presupuesto</button>",
        ),
        (
            "<p class=\"text-xs text-slate-500\">Formulario demo. En Odoo se conectará a CRM/Form real.</p>",
            f"<div class=\"flex flex-col gap-2\">\n              <p class=\"text-xs text-slate-500\">Formulario conectado a Odoo (endpoint de ejemplo). No mostramos el email en la página.</p>\n              <a href=\"tel:{PHONE_TEL}\" class=\"text-xs text-slate-300 hover:text-white\">O si lo prefieres: llamar al {PHONE_DISPLAY}</a>\n            </div>",
        ),
    ]
    return replace_all(content, pairs)


def transform_v2(content: str) -> str:
    pairs = [
        (
            "<title>Cableado de Redes | Instalación y certificación</title>",
            f"<title>{META_TITLE_DEFAULT}</title>",
        ),
        (
            "<meta name=\"description\" content=\"Cableado estructurado para empresas: Cat6/Cat6A/fibra, racks, patch panels, WiFi y documentación.\" />",
            f"<meta name=\"description\" content=\"{META_DESC_DEFAULT}\" />",
        ),
        (
            "Visita técnica + documentación",
            "Madrid · visita técnica + documentación",
        ),
        (
            "Cableado de redes para empresas,\n          <span class=\"text-transparent bg-clip-text bg-gradient-to-r from-brand-700 to-cyan-600\">hecho bien</span>",
            "Cableado de <span class=\"text-transparent bg-clip-text bg-gradient-to-r from-brand-700 to-cyan-600\">redes informáticas</span>\n          en Madrid (Cat6/Cat6A y fibra)",
        ),
        (
            "Instalación de cableado estructurado (Cat6/Cat6A/fibra), racks y WiFi. Etiquetado, orden y pruebas para una red estable y ampliable.",
            "Instalación de <strong>cableado de redes informáticas</strong> en <strong>Madrid</strong>: puntos RJ45 (Cat6/Cat6A), fibra (si aplica), racks y WiFi. "
            "Etiquetado, pruebas y documentación para una red estable y ampliable.",
        ),
        (
            ">Solicitar visita</a>",
            ">Solicitar presupuesto</a>",
        ),
        (
            "<h2 class=\"text-3xl font-extrabold tracking-tight\">Pide presupuesto</h2>",
            "<h2 class=\"text-3xl font-extrabold tracking-tight\">Solicita presupuesto en Madrid</h2>",
        ),
        (
            "Rellena esto (demo) y lo conectamos a tu formulario/CRM en Odoo.",
            "Cuéntanos el nº de puestos, si ya hay canalización y el tipo de espacio. Te respondemos en ≤ 24h laborables.",
        ),
        (
            "<form class=\"rounded-2xl border border-slate-200 bg-slate-50 p-6\">",
            f"<form method=\"post\" action=\"{ODOO_PLACEHOLDER}\" class=\"rounded-2xl border border-slate-200 bg-slate-50 p-6\">",
        ),
        (
            "<div><label class=\"text-xs text-slate-600\">Nombre</label><input class=\"mt-1 w-full rounded-xl border border-slate-200 bg-white px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"Tu nombre\" /></div>\n            <div><label class=\"text-xs text-slate-600\">Email o teléfono</label><input class=\"mt-1 w-full rounded-xl border border-slate-200 bg-white px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"nombre@empresa.com\" /></div>\n            <div><label class=\"text-xs text-slate-600\">Mensaje</label><textarea rows=\"4\" class=\"mt-1 w-full rounded-xl border border-slate-200 bg-white px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"Ej.: 12 puntos, 1 rack, Cat6A...\"></textarea></div>",
            "<div><label class=\"text-xs text-slate-600\">Nombre y apellidos</label><input name=\"name\" required autocomplete=\"name\" class=\"mt-1 w-full rounded-xl border border-slate-200 bg-white px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"Tu nombre\" /></div>\n            "
            "<div><label class=\"text-xs text-slate-600\">Teléfono</label><input name=\"phone\" required autocomplete=\"tel\" class=\"mt-1 w-full rounded-xl border border-slate-200 bg-white px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"+34 ...\" /></div>\n            "
            "<div><label class=\"text-xs text-slate-600\">Email</label><input name=\"email_from\" type=\"email\" required autocomplete=\"email\" class=\"mt-1 w-full rounded-xl border border-slate-200 bg-white px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"tu@empresa.com\" /></div>\n            "
            "<div><label class=\"text-xs text-slate-600\">Mensaje</label><textarea name=\"description\" rows=\"4\" required class=\"mt-1 w-full rounded-xl border border-slate-200 bg-white px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"Ej.: 20 puestos, canaleta existente, rack 12U, 2 APs PoE, Cat6A...\"></textarea></div>\n            "
            "<input type=\"hidden\" name=\"x_service\" value=\"Cableado de redes informáticas\" />\n            "
            "<input type=\"hidden\" name=\"x_city\" value=\"Madrid\" />",
        ),
        (
            "<button type=\"button\" class=\"inline-flex w-full items-center justify-center rounded-xl bg-brand-600 px-5 py-3 text-sm font-semibold text-white hover:bg-brand-700\">Enviar (demo)</button>",
            "<button type=\"submit\" class=\"inline-flex w-full items-center justify-center rounded-xl bg-brand-600 px-5 py-3 text-sm font-semibold text-white hover:bg-brand-700\">Solicitar presupuesto</button>",
        ),
        (
            "<p class=\"text-xs text-slate-500\">Formulario demo.</p>",
            f"<div class=\"flex flex-col gap-2\">\n              <p class=\"text-xs text-slate-500\">Formulario conectado a Odoo (endpoint de ejemplo). No mostramos el email en la página.</p>\n              <a href=\"tel:{PHONE_TEL}\" class=\"text-xs text-slate-600 hover:text-slate-900\">O si lo prefieres: llamar al {PHONE_DISPLAY}</a>\n            </div>",
        ),
    ]
    return replace_all(content, pairs)


def transform_v3(content: str) -> str:
    pairs = [
        (
            "<title>Cableado de Redes Industrial | Cat6A · Fibra · Racks</title>",
            "<title>Cableado de redes informáticas en Madrid | Industrial · Cat6A · Fibra</title>",
        ),
        (
            "<meta name=\"description\" content=\"Cableado estructurado para industria y logística: Cat6A/fibra, racks, patching, pruebas y documentación.\" />",
            f"<meta name=\"description\" content=\"{META_DESC_DEFAULT}\" />",
        ),
        (
            "Cat6A · Fibra · Racks · Etiquetado",
            "Madrid · Cat6A · Fibra · Racks · Checklist",
        ),
        (
            "Cableado estructurado\n          <span class=\"text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-yellow-200\">para entornos exigentes</span>",
            "Cableado de <span class=\"text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-yellow-200\">redes informáticas</span>\n          en Madrid (Cat6A + fibra)",
        ),
        (
            "Instalación para naves, logística y oficinas técnicas. Orden, pruebas y documentación para una red mantenible.",
            "Instalación de <strong>cableado de redes informáticas</strong> en <strong>Madrid</strong> para naves, logística, oficinas y centros de trabajo. Orden, pruebas y documentación para una red mantenible.",
        ),
        (
            ">Solicitar visita técnica</a>",
            ">Solicitar presupuesto</a>",
        ),
        (
            "<h2 class=\"text-3xl font-extrabold tracking-tight\">¿Te pasamos una propuesta?</h2>",
            "<h2 class=\"text-3xl font-extrabold tracking-tight\">Solicita presupuesto en Madrid</h2>",
        ),
        (
            "Demo. Lo conectamos a Odoo Forms/CRM cuando toque.",
            "Cuéntanos el alcance (puntos, canalización, rack, PoE/WiFi). Te respondemos en ≤ 24h laborables.",
        ),
        (
            "<form class=\"rounded-2xl border border-white/10 bg-slate-950/30 p-6\">",
            f"<form method=\"post\" action=\"{ODOO_PLACEHOLDER}\" class=\"rounded-2xl border border-white/10 bg-slate-950/30 p-6\">",
        ),
        (
            "<div><label class=\"text-xs text-slate-400\">Nombre</label><input class=\"mt-1 w-full rounded-xl border border-white/10 bg-slate-950/40 px-4 py-2 text-sm text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"Tu nombre\" /></div>\n            <div><label class=\"text-xs text-slate-400\">Email o teléfono</label><input class=\"mt-1 w-full rounded-xl border border-white/10 bg-slate-950/40 px-4 py-2 text-sm text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"nombre@empresa.com\" /></div>\n            <div><label class=\"text-xs text-slate-400\">Detalle</label><textarea rows=\"4\" class=\"mt-1 w-full rounded-xl border border-white/10 bg-slate-950/40 px-4 py-2 text-sm text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"Ej.: 30 puntos, fibra a oficinas, 2 racks...\"></textarea></div>",
            "<div><label class=\"text-xs text-slate-400\">Nombre y apellidos</label><input name=\"name\" required autocomplete=\"name\" class=\"mt-1 w-full rounded-xl border border-white/10 bg-slate-950/40 px-4 py-2 text-sm text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"Tu nombre\" /></div>\n            "
            "<div><label class=\"text-xs text-slate-400\">Teléfono</label><input name=\"phone\" required autocomplete=\"tel\" class=\"mt-1 w-full rounded-xl border border-white/10 bg-slate-950/40 px-4 py-2 text-sm text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"+34 ...\" /></div>\n            "
            "<div><label class=\"text-xs text-slate-400\">Email</label><input name=\"email_from\" type=\"email\" required autocomplete=\"email\" class=\"mt-1 w-full rounded-xl border border-white/10 bg-slate-950/40 px-4 py-2 text-sm text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"tu@empresa.com\" /></div>\n            "
            "<div><label class=\"text-xs text-slate-400\">Mensaje</label><textarea name=\"description\" rows=\"4\" required class=\"mt-1 w-full rounded-xl border border-white/10 bg-slate-950/40 px-4 py-2 text-sm text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-brand-500\" placeholder=\"Ej.: 60 puntos, bandeja, fibra entre racks, PoE para APs/cámaras...\"></textarea></div>\n            "
            "<input type=\"hidden\" name=\"x_service\" value=\"Cableado de redes informáticas\" />\n            "
            "<input type=\"hidden\" name=\"x_city\" value=\"Madrid\" />",
        ),
        (
            "<button type=\"button\" class=\"inline-flex w-full items-center justify-center rounded-xl bg-brand-500 px-5 py-3 text-sm font-semibold text-slate-950 hover:bg-brand-400\">Enviar (demo)</button>",
            "<button type=\"submit\" class=\"inline-flex w-full items-center justify-center rounded-xl bg-brand-500 px-5 py-3 text-sm font-semibold text-slate-950 hover:bg-brand-400\">Solicitar presupuesto</button>",
        ),
        (
            "<p class=\"text-xs text-slate-500\">Formulario demo.</p>",
            f"<div class=\"flex flex-col gap-2\">\n              <p class=\"text-xs text-slate-500\">Formulario conectado a Odoo (endpoint de ejemplo). No mostramos el email en la página.</p>\n              <a href=\"tel:{PHONE_TEL}\" class=\"text-xs text-slate-300 hover:text-white\">O si lo prefieres: llamar al {PHONE_DISPLAY}</a>\n            </div>",
        ),
    ]
    return replace_all(content, pairs)


def main() -> None:
    variants = [
        ("v1-dark.html", "v1-dark-madrid.html", transform_v1),
        ("v2-light.html", "v2-light-madrid.html", transform_v2),
        ("v3-industrial.html", "v3-industrial-madrid.html", transform_v3),
    ]

    for src, dst, fn in variants:
        src_p = Path(src)
        dst_p = Path(dst)
        content = src_p.read_text(encoding="utf-8")
        out = fn(content)
        dst_p.write_text(out, encoding="utf-8")
        print(f"wrote {dst} ({len(out)} chars)")


if __name__ == "__main__":
    main()
