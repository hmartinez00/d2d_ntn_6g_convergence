import matplotlib.pyplot as plt
import numpy as np

# --- 1. CONFIGURACIÓN DE DATOS REAUSTADOS ---
years = np.array([2022, 2023, 2024, 2025, 2026])

# Serie Principal: Azul Cobalto (Crecimiento Exponencial Inflexión 2023)
gen_ai_llms = np.array([7, 12, 43, 85, 142])

# Serie Secundaria: Gris Técnico (Crecimiento Sostenido)
marl_agents = np.array([23, 33, 45, 56, 65])

# Serie Terciaria: Negra (Crecimiento Sostenido Inferior)
osam_archs = np.array([7, 12, 26, 37, 49])

# --- 2. CONFIGURACIÓN ESTÉTICA ESTÁNDAR IEEE (MATPLOTLIB) ---
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.linewidth": 1.2,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.major.size": 5,
    "ytick.major.size": 5
})

colors = {
    'cobalt_blue': '#0047AB',
    'tech_gray': '#4A4A4A',
    'black_line': '#000000'
}

fig, ax = plt.subplots(figsize=(10, 5.5), dpi=150)

# --- GENERACIÓN DE SERIES ---
ax.plot(years, gen_ai_llms, color=colors['cobalt_blue'], marker='o', markersize=8,
        linewidth=2.5, label='Cobalt blue', markerfacecolor='white', markeredgewidth=2.5, zorder=5)

ax.plot(years, marl_agents, color=colors['tech_gray'], marker='s', markersize=7,
        linewidth=2.0, label='Technical Gray', markerfacecolor='white', markeredgewidth=2.0, zorder=4)

ax.plot(years, osam_archs, color=colors['black_line'], marker='^', markersize=8,
        linewidth=2.0, label='Black line', markerfacecolor='white', markeredgewidth=2.0, zorder=3)

# --- ESTILIZACIÓN DE EJES ---
ax.set_xlabel('Year', labelpad=10)
ax.set_ylabel('Number of Indexed Publications (Est.)', labelpad=10)

ax.set_xticks(years)
ax.set_xlim(2021.8, 2026.2)
ax.set_ylim(0, 150)
ax.set_yticks(np.arange(0, 151, 50))

# Cuadrícula horizontal tenue
ax.grid(axis='y', linestyle='-', alpha=0.2)

# Esquinas e interconexiones limpias estilo IEEE
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# --- LEYENDA TÉCNICA CUADRADA ---
ax.legend(loc='upper left', frameon=True, fancybox=False, edgecolor='black', framealpha=1, fontsize=10)

# Anotación del Hito Tecnológico (Post-2023)
ax.annotate('Global technology hito', xy=(2023, 13), xytext=(2022.2, 70),
            arrowprops=dict(arrowstyle='->', color='black', linewidth=1.2),
            color='black', fontsize=10)

plt.tight_layout()
plt.show()

# --- 3. GENERADOR AUTOMÁTICO DE CÓDIGO TIKZ ---
def export_to_tikz():
    print("\n" + "="*45)
    print(" CÓDIGO TIKZ GENERADO (FIEL A LA IMAGEN) ")
    print("="*45 + "\n")

    def format_coords(x_data, y_data):
        return "".join([f"({x},{y})" for x, y in zip(x_data, y_data)])

    tikz_template = f"""\\definecolor{{cobaltblue}}{{HTML}}{{0047AB}}
\\definecolor{{techgray}}{{HTML}}{{4A4A4A}}

\\begin{{tikzpicture}}
\\begin{{axis}}[
    width=\\linewidth,
    height=6.5cm,
    grid=major,
    grid style={{line width=.1pt, draw=gray!20}},
    xlabel={{Year}},
    ylabel={{Number of Indexed Publications (Est.)}},
    xmin=2022, xmax=2026,
    ymin=0, ymax=150,
    xtick={{2022, 2023, 2024, 2025, 2026}},
    ytick={{0, 50, 100, 150}},
    tick pos=left,
    xtick align=inside,
    ytick align=inside,
    legend pos=north west,
    legend style={{draw=black, fill=white, font=\\footnotesize, fancybox=false, cells={{anchor=west}}}},
    axis x line=bottom,
    axis y line=left,
    clip=false
]

% Serie Cobalt Blue
\\addplot[cobaltblue, line width=1.5pt, mark=*, mark options={{fill=white, line width=1.5pt, scale=1.2}}] coordinates {{{format_coords(years, gen_ai_llms)}}};
\\addlegendentry{{Cobalt blue}}

% Serie Technical Gray
\\addplot[techgray, line width=1.2pt, mark=square*, mark options={{fill=white, line width=1.2pt, scale=1.1}}] coordinates {{{format_coords(years, marl_agents)}}};
\\addlegendentry{{Technical Gray}}

% Serie Black Line
\\addplot[black, line width=1.2pt, mark=triangle*, mark options={{fill=white, line width=1.2pt, scale=1.2}}] coordinates {{{format_coords(years, osam_archs)}}};
\\addlegendentry{{Black line}}

% Flecha y etiqueta de hito tecnológico
\\draw[->, >=stealth, black, thick] (axis cs:2022.8, 65) -- (axis cs:2023, 16);
\\node[black, font=\\small, anchor=south east] at (axis cs:2022.9, 65) {{Global technology hito}};

\\end{{axis}}
\\end{{tikzpicture}}"""
    
    print(tikz_template)

export_to_tikz()