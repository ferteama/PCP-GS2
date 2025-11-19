from stages import Carreira, Model
from repo import ModelRepository
from stages import Carreira 


class Main:
    def __init__(self):
        self.repo = ModelRepository()

    def _ask_bool(self, text):
        """Converte respostas como 's', 'sim', '1' em True."""
        resp = input(text + " (s/n): ").strip().lower()
        return resp in ["s", "sim", "1", "y", "yes"]

    # Adiciona um novo lead
    def add_profiles(self):
        print("\n=== Adicionar Lead ===")

        nome = input("Nome: ").strip()
        email = input("E-mail: ").strip()

        if not nome or not email or "@" not in email:
            print("Nome e e-mail válidos são obrigatórios.")
            return

        # Entradas booleanas (todas s/n)
        interesse = self._ask_bool("Possui interesse em tecnologia?")
        criatividade = self._ask_bool("Possui um nível considerável de criatividade?")
        logica = self._ask_bool("Possui um nível considerável de lógica?")
        afinidade = self._ask_bool("Possui um nível considerável de afinidade com pessoas?")
        adaptabilidade = self._ask_bool("Possui um nível considerável de adaptabilidade a casos adversos?")

        # Criação da pessoa
        pessoa = Carreira(
            nome=nome,
            email=email,
            criatividade=criatividade,
            interesse=interesse,
            logica=logica,
            afinidade=afinidade,
            adaptabilidade=adaptabilidade
        )

        # Modelo
        profiles = Model(pessoa=pessoa, stage="novo")

        # Salvar
        self.repo.add_profiles(profiles.to_dict())

        print(f"\nPerfil adicionado com sucesso! (Área sugerida: {pessoa.area()})")

    # Lista todos os Perfis
    def list_profiles(self):
        print("\n=== Lista de Perfis ===")
        profiles = self.repo.read_profiles()

        if not profiles:
            print("Nenhum perfil cadastrado.")
            return

        print(f"\n{'#':<3} {'Nome':<20} {'E-mail':<30} {'Área':<25} {'Interesse':<10}")
        print("-" * 90)

        for i, l in enumerate(profiles):
            print(
                f"{i:<3} {l['name']:<20} {l['email']:<30} "
                f"{l.get('perfil_type', '—'):<25} {str(l.get('interesse', '—'))}"
            )

    # Busca perfil por nome ou e-mail
    def search_profiles(self):
        print("\n=== Buscar Perfis ===")
        q = input("Buscar por: ").strip()

        if not q:
            print("Consulta vazia.")
            return

        results = self.repo.search_profiles(q)

        if not results:
            print("Nenhum resultado encontrado.")
            return

        print(f"\n{'#':<3} {'Nome':<20} {'E-mail':<30} {'Área':<25} {'Interesse':<10}")
        print("-" * 90)

        for i, l in enumerate(results):
            print(
                f"{i:<3} {l['name']:<20} {l['email']:<30} "
                f"{l.get('perfil_type', '—'):<25} {str(l.get('interesse', '—'))}"
            )

    def show_areas(self):
        print("\n=== Áreas Disponíveis ===")
        areas = list(Carreira.AREAS_RESUMO.keys())  
        
        for i, area in enumerate(areas):
            print(f"{i+1}. {area}")
        escolha = input("\nEscolha uma área para ver o resumo (0 para voltar): ").strip()
        if escolha == "0" or escolha == "":
            return
        try:
            idx = int(escolha) - 1
            if idx < 0 or idx >= len(areas):
                print("Opção inválida.")
                return
        except ValueError:
            print("Entrada inválida.")
            return
        area_escolhida = areas[idx]
        print(f"\n=== {area_escolhida} ===")
        print(Carreira.AREAS_RESUMO[area_escolhida])  
        
        # Mostrar perfis cadastrados nessa área
        profiles = self.repo.read_profiles()
        filtrados = [p for p in profiles if p.get("perfil_type") == area_escolhida]
        
        if filtrados:
            print("\nPerfis nessa área:")
            for p in filtrados:
                print(f"- {p['name']} ({p['email']})")
        else:
            print("\nNenhum perfil cadastrado nessa área ainda.")
        


    def run(self):
        while True:
            print_menu()
            op = input("Escolha: ").strip()

            if op == "1":
                self.add_profiles()
            elif op == "2":
                self.list_profiles()
            elif op == "3":
                self.search_profiles()
            elif op == "4":
                self.show_areas()
            elif op == "0":
                print("\nAté mais!")
                break
            else:
                print("Opção inválida.")


def print_menu():
    print("\nAgente de Carreira Adaptativa (ACA)")
    print("[1] Adicionar Perfil")
    print("[2] Listar Perfis")
    print("[3] Buscar Perfis")
    print("[4] Exibir Áreas Disponíveis")
    print("[0] Sair")


if __name__ == "__main__":
    Main().run()
