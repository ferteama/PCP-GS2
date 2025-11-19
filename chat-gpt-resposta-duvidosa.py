#!/usr/bin/env python3
"""
career_recommender.py

Sistema OOP em Python que organiza e analisa perfis profissionais do futuro.
Uso: python career_recommender.py
"""

import json
from typing import Dict, List, Tuple, Any
from pathlib import Path


# Competências padrão (tupla imutável)
COMPETENCIAS: Tuple[str, ...] = (
    "logica",
    "criatividade",
    "colaboracao",
    "adaptabilidade",
    "comunicacao",
    "produto",
    "ciência_de_dados",
    "engenharia_de_software",
    "ux",
    "infraestrutura",
)

# Banco de carreiras com pesos por competência (dicionário)
# Pesos: 0..5 (importância da competência para a carreira)
CAREERS: List[Dict[str, Any]] = [
    {
        "nome": "Engenheiro de Machine Learning",
        "descricao": "Desenvolve modelos de ML, produção e pipelines de dados.",
        "pesos": {
            "logica": 5,
            "ciência_de_dados": 5,
            "engenharia_de_software": 4,
            "infraestrutura": 3,
            "comunicacao": 2,
            "criatividade": 3,
        },
        "trilha": [
            "Curso de Python para Data Science",
            "Fundamentos de Machine Learning",
            "Deploy de modelos (MLOps)",
        ],
    },
    {
        "nome": "Designer de Experiência (UX/UI)",
        "descricao": "Projeta experiências centradas no usuário.",
        "pesos": {
            "ux": 5,
            "criatividade": 5,
            "comunicacao": 4,
            "colaboracao": 4,
            "produto": 3,
        },
        "trilha": [
            "Princípios de UX",
            "Design de Interfaces",
            "Pesquisa com usuários",
        ],
    },
    {
        "nome": "Engenheiro de Software",
        "descricao": "Constrói sistemas, API's e software robusto.",
        "pesos": {
            "engenharia_de_software": 5,
            "logica": 4,
            "colaboracao": 4,
            "infraestrutura": 3,
            "comunicacao": 2,
        },
        "trilha": [
            "Estruturas de Dados e Algoritmos",
            "Desenvolvimento Web/Backend",
            "Arquitetura de Software",
        ],
    },
    {
        "nome": "Product Manager",
        "descricao": "Define visão do produto e coordena times multidisciplinares.",
        "pesos": {
            "produto": 5,
            "comunicacao": 5,
            "colaboracao": 4,
            "criatividade": 3,
            "adaptabilidade": 3,
        },
        "trilha": [
            "Fundamentos de Product Management",
            "Métricas de produto",
            "Entrevistas com usuários e discovery",
        ],
    },
    {
        "nome": "Especialista em Infraestrutura / DevOps",
        "descricao": "Garante disponibilidade e escalabilidade de sistemas.",
        "pesos": {
            "infraestrutura": 5,
            "engenharia_de_software": 4,
            "logica": 3,
            "colaboracao": 3,
        },
        "trilha": [
            "Linux e Redes",
            "Containers e Orquestração (Docker, Kubernetes)",
            "CI/CD e Observability",
        ],
    },
]


# ---------- Classes de domínio ----------

class Competencia:
    """Representa uma competência com um valor (0..5)."""

    def __init__(self, nome: str, valor: int = 0):
        if nome not in COMPETENCIAS:
            raise ValueError(f"Competência '{nome}' não reconhecida.")
        self.nome = nome
        self.valor = max(0, min(5, int(valor)))

    def to_dict(self) -> Dict[str, Any]:
        return {"nome": self.nome, "valor": self.valor}


class Perfil:
    """Representa um perfil profissional com um conjunto de competências."""

    def __init__(self, nome: str, email: str = ""):
        self.nome = nome
        self.email = email
        # Armazena competências como dict: nome -> Competencia
        self.competencias: Dict[str, Competencia] = {
            c: Competencia(c, 0) for c in COMPETENCIAS
        }
        self.observacoes: str = ""

    def set_competencia(self, nome: str, valor: int):
        if nome not in self.competencias:
            raise KeyError(f"Competência '{nome}' inválida.")
        self.competencias[nome].valor = max(0, min(5, int(valor)))

    def get_score_dict(self) -> Dict[str, int]:
        return {n: c.valor for n, c in self.competencias.items()}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "nome": self.nome,
            "email": self.email,
            "competencias": self.get_score_dict(),
            "observacoes": self.observacoes,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Perfil":
        p = cls(data["nome"], data.get("email", ""))
        comps = data.get("competencias", {})
        for k, v in comps.items():
            if k in p.competencias:
                p.set_competencia(k, v)
        p.observacoes = data.get("observacoes", "")
        return p


class Recomendador:
    """Gera recomendações de carreira baseado nas competências do perfil."""

    def __init__(self, careers_db: List[Dict[str, Any]] = None):
        self.careers = careers_db if careers_db is not None else CAREERS

    @staticmethod
    def _score_for_career(profile: Perfil, career: Dict[str, Any]) -> float:
        """Calcula um score entre 0 e 100 para o career dado o perfil."""
        weights: Dict[str, int] = career.get("pesos", {})
        if not weights:
            return 0.0
        total_weight = sum(weights.values())
        if total_weight == 0:
            return 0.0
        # soma ponderada das competências (valor 0..5)
        total = 0.0
        for comp, w in weights.items():
            user_val = profile.competencias.get(comp, Competencia(comp, 0)).valor
            total += user_val * w
        # Normalizar para 0..100
        max_possible = 5 * total_weight
        return (total / max_possible) * 100.0

    def rank_careers(self, profile: Perfil, top_n: int = 3) -> List[Tuple[Dict[str, Any], float]]:
        """Retorna lista de (career, score) ordenada decrescente."""
        scored = []
        for career in self.careers:
            sc = self._score_for_career(profile, career)
            scored.append((career, sc))
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_n]

    def suggested_improvements(self, profile: Perfil, career: Dict[str, Any], n: int = 3) -> List[Tuple[str, int, int]]:
        """
        Para uma carreira, sugere N competências para melhorar baseadas na diferença
        entre peso da carreira e valor atual do usuário.
        Retorna lista de (competência, valor_atual, peso).
        """
        weights = career.get("pesos", {})
        # calcular prioridade por (peso * (5 - atual_valor))
        deficits = []
        for comp, w in weights.items():
            atual = profile.competencias.get(comp, Competencia(comp, 0)).valor
            potencial_ganho = w * (5 - atual)
            deficits.append((comp, atual, w, potencial_ganho))
        # ordenar por potencial_ganho decrescente
        deficits.sort(key=lambda x: x[3], reverse=True)
        # retornar top n (nome, atual, peso)
        return [(d[0], d[1], d[2]) for d in deficits[:n]]


# ---------- Persistência simples (JSON) ----------

DATA_FILE = Path("perfis.json")


def load_profiles() -> List[Perfil]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Perfil.from_dict(item) for item in data]


def save_profiles(profiles: List[Perfil]):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([p.to_dict() for p in profiles], f, ensure_ascii=False, indent=2)


# ---------- Interface de linha de comando (CLI) ----------

def print_line():
    print("-" * 60)


def mostrar_competencias():
    print_line()
    print("Competências disponíveis (0..5):")
    for i, c in enumerate(COMPETENCIAS, start=1):
        print(f"{i:2d}. {c}")
    print_line()


def criar_perfil_interativo() -> Perfil:
    nome = input("Nome: ").strip()
    email = input("Email (opcional): ").strip()
    perfil = Perfil(nome, email)
    print("Defina suas competências (0..5). Aperte Enter para pular (fica 0).")
    for c in COMPETENCIAS:
        while True:
            try:
                s = input(f"{c} (0..5): ").strip()
                if s == "":
                    break
                v = int(s)
                if 0 <= v <= 5:
                    perfil.set_competencia(c, v)
                    break
                else:
                    print("Valor deve ser entre 0 e 5.")
            except ValueError:
                print("Entrada inválida. Digite um inteiro 0..5 ou Enter.")
    perfil.observacoes = input("Observações (opcional): ").strip()
    return perfil


def escolher_perfil(profiles: List[Perfil]) -> Perfil:
    if not profiles:
        print("Nenhum perfil cadastrado.")
        return None
    for idx, p in enumerate(profiles, start=1):
        print(f"{idx}. {p.nome} ({p.email})")
    while True:
        try:
            s = input("Escolha número do perfil (ou 0 para cancelar): ").strip()
            if s == "0" or s == "":
                return None
            i = int(s)
            if 1 <= i <= len(profiles):
                return profiles[i - 1]
        except ValueError:
            pass
        print("Opção inválida.")


def exibir_recomendacoes(profile: Perfil, recomendador: Recomendador):
    print_line()
    print(f"Recomendações para: {profile.nome}")
    ranked = recomendador.rank_careers(profile, top_n=5)
    for idx, (career, score) in enumerate(ranked, start=1):
        print_line()
        print(f"{idx}. {career['nome']}  —  Score: {score:.1f}%")
        print(f"   Descrição: {career.get('descricao','')}")
        print("   Trilha sugerida:")
        for passo in career.get("trilha", []):
            print(f"     - {passo}")
        # sugestões de melhoria
        sugeridas = recomendador.suggested_improvements(profile, career, n=3)
        if sugeridas:
            print("   Competências para focar (atual -> peso):")
            for comp, atual, peso in sugeridas:
                print(f"     - {comp}: {atual} -> peso {peso}")
    print_line()


def main_cli():
    profiles = load_profiles()
    recomendador = Recomendador()
    while True:
        print("\nSistema de Recomendação de Carreiras — Menu")
        print("1) Cadastrar novo perfil")
        print("2) Listar perfis")
        print("3) Avaliar / editar perfil")
        print("4) Gerar recomendações para um perfil")
        print("5) Salvar perfis")
        print("6) Carregar perfis (do arquivo)")
        print("7) Sair")
        choice = input("Escolha: ").strip()
        if choice == "1":
            p = criar_perfil_interativo()
            profiles.append(p)
            print(f"Perfil '{p.nome}' cadastrado.")
        elif choice == "2":
            if not profiles:
                print("Nenhum perfil cadastrado.")
            else:
                print_line()
                for i, p in enumerate(profiles, start=1):
                    print(f"{i}. {p.nome} — {p.email}")
                    sc = p.get_score_dict()
                    # resumir média das competências
                    media = sum(sc.values()) / (len(sc) or 1)
                    print(f"   Média competências: {media:.2f} (0..5)")
                print_line()
        elif choice == "3":
            p = escolher_perfil(profiles)
            if p is None:
                continue
            print(f"Editando perfil: {p.nome}")
            mostrar_competencias()
            for c in COMPETENCIAS:
                atual = p.competencias[c].valor
                s = input(f"{c} atual={atual}. Novo valor (0..5 ou Enter p/ manter): ").strip()
                if s != "":
                    try:
                        v = int(s)
                        if 0 <= v <= 5:
                            p.set_competencia(c, v)
                        else:
                            print("Valor fora do intervalo, mantendo atual.")
                    except ValueError:
                        print("Entrada inválida, mantendo atual.")
            obs = input("Observações (Enter para manter): ").strip()
            if obs != "":
                p.observacoes = obs
            print("Perfil atualizado.")
        elif choice == "4":
            p = escolher_perfil(profiles)
            if p is None:
                continue
            exibir_recomendacoes(p, recomendador)
        elif choice == "5":
            save_profiles(profiles)
            print(f"Perfis salvos em {DATA_FILE.resolve()}")
        elif choice == "6":
            profiles = load_profiles()
            print(f"Perfis carregados ({len(profiles)} encontrados).")
        elif choice == "7":
            print("Saindo. Não se esqueça de salvar (opção 5) se quiser persistir.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main_cli()
