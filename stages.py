from datetime import date


class Perfil:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    def area(self):
        """Retorna área padrão caso nenhuma regra seja aplicada."""
        return "Indefinida"

    def exibir_informacoes(self):
        return f"Nome: {self.nome} | E-mail: {self.email}"


class Competencia(Perfil):
    def __init__(self, nome: str, email: str, criatividade: bool, interesse: bool, logica: bool, afinidade: bool, adaptabilidade: bool):
        super().__init__(nome, email)
        self.criatividade = criatividade
        self.interesse = interesse
        self.logica = logica
        self.afinidade = afinidade
        self.adaptabilidade = adaptabilidade

    def exibir_informacoes(self):
        return (
            f"Nome: {self.nome} | E-mail: {self.email} | "
            f"Criatividade: {self.criatividade} | Interesse: {self.interesse} | "
            f"Lógica: {self.logica} | Afinidade: {self.afinidade} | "
            f"Adaptabilidade: {self.adaptabilidade}"
        )


class Carreira(Competencia):
    def __init__(self, nome: str, email: str, criatividade: bool, interesse: bool, logica: bool, afinidade: bool, adaptabilidade: bool):
        super().__init__(nome, email, criatividade, interesse, logica, afinidade, adaptabilidade)
        # 1
        self.rh = afinidade and criatividade and not interesse and not logica and not adaptabilidade  
        # 2
        self.tecnicoautomocao = logica and adaptabilidade and not criatividade and not interesse and not afinidade  
        # 3
        self.analistaCS = logica and afinidade and not criatividade and not interesse and not adaptabilidade
        # 4
        self.tecnicoindustrial = logica and afinidade and adaptabilidade and not criatividade and not interesse 
        # 5
        self.suportetecnico = interesse and adaptabilidade and not criatividade and not logica and not afinidade  
        # 6
        self.professor = interesse and afinidade and not criatividade and not logica and not adaptabilidade 
        # 7
        self.productmanager = interesse and afinidade and adaptabilidade and not criatividade and not logica  
        # 8
        self.cientistadados = interesse and logica and not criatividade and not afinidade and not adaptabilidade 
        # 9
        self.analistabi = interesse and logica and adaptabilidade and not criatividade and not afinidade  
        # 10
        self.analistadenegocios = interesse and logica and afinidade and not criatividade and not adaptabilidade  
        # 11
        self.gestorprojetos = logica and afinidade and adaptabilidade and interesse and not criatividade  
        # 12
        self.artistadigital = criatividade and afinidade and not interesse and not logica and not adaptabilidade 
        # 13
        self.marketing = criatividade and afinidade and not interesse and not logica and not adaptabilidade
        # 14
        self.designerexp = criatividade and afinidade and adaptabilidade and not interesse and not logica 
        # 15
        self.gamedesigner = criatividade and logica and not interesse and not afinidade and not adaptabilidade
        # 16
        self.programadorclp = criatividade and logica and adaptabilidade and not interesse and not afinidade 
        # 17
        self.analistadigital = criatividade and afinidade and logica and not interesse and not adaptabilidade
        # 18
        self.arquitetoinf = criatividade and afinidade and adaptabilidade and logica and not interesse
        # 19
        self.analistaproduto = criatividade and interesse and not logica and not afinidade and not adaptabilidade
        # 20
        self.produtorcd = criatividade and interesse and adaptabilidade and not logica and not afinidade
        # 21
        self.devops = criatividade and interesse and afinidade and not logica and not adaptabilidade
        # 22
        self.gpm = criatividade and interesse and afinidade and adaptabilidade and not logica
        # 23
        self.engenheiroia = criatividade and interesse and logica and not afinidade and not adaptabilidade
        # 24
        self.engenheiroinovacao = criatividade and interesse and logica and adaptabilidade and not afinidade
        # 25
        self.desenvolvedorgames = criatividade and interesse and logica and afinidade and not adaptabilidade
        # 26
        self.liderinocacao = criatividade and interesse and logica and afinidade and adaptabilidade

    def area(self):
        if self.rh:
            return "RH"
        if self.tecnicoautomocao:
            return "Técnico em Automação / Automação Industrial"
        if self.analistaCS:
            return "Analista de Customer Success"
        if self.tecnicoindustrial:
            return "Técnico em Automação / Automação Industrial"
        if self.suportetecnico:
            return "Suporte Técnico Avançado"
        if self.professor:
            return "Professor de Tecnologia"
        if self.productmanager:
            return "Product Manager"
        if self.cientistadados:
            return "Cientista de Dados"
        if self.analistabi:
            return "Analista de BI"
        if self.analistadenegocios:
            return "Analista de Negócios"
        if self.gestorprojetos:
            return "Gestor de Projetos"
        if self.artistadigital:
            return "Artista Digital"
        if self.marketing:
            return "Profissional de Marketing / Comunicação"
        if self.designerexp:
            return "Designer de Experiência"
        if self.gamedesigner:
            return "Game Designer"
        if self.programadorclp:
            return "Programador de CLP"
        if self.analistadigital:
            return "Analista Digital"
        if self.arquitetoinf:
            return "Arquiteto de Infraestrutura"
        if self.analistaproduto:
            return "Analista de Produto"
        if self.produtorcd:
            return "Produtor de Conteúdo Digital"
        if self.devops:
            return "DevOps"
        if self.gpm:
            return "Gerente de Produto de Marketing"
        if self.engenheiroia:
            return "Engenheiro de IA"
        if self.engenheiroinovacao:
            return "Engenheiro de Inovação"
        if self.desenvolvedorgames:
            return "Desenvolvedor de Games"
        if self.liderinocacao:
            return "Líder de Inovação"
        else:
            return "Sem recomendação!"
        
    AREAS_RESUMO = {
    "RH": "Área focada em gestão de pessoas, recrutamento e desenvolvimento humano.",
    "Técnico em Automação / Automação Industrial": "Trabalha com sistemas automatizados, sensores e controle.",
    "Analista de Customer Success": "Ajuda clientes a obter o máximo valor de produtos e serviços.",
    "Suporte Técnico Avançado": "Atua na resolução de problemas técnicos e atendimento especializado.",
    "Professor de Tecnologia": "Ensina conceitos técnicos e desenvolve habilidades digitais em alunos.",
    "Product Manager": "Define visão do produto e coordena times para alcançar objetivos.",
    "Cientista de Dados": "Analisa grandes volumes de dados e desenvolve modelos estatísticos.",
    "Analista de BI": "Transforma dados em insights estratégicos e dashboards.",
    "Analista de Negócios": "Faz ponte entre stakeholders e tecnologia, levantando requisitos.",
    "Gestor de Projetos": "Gerencia cronogramas, riscos, recursos e entregas.",
    "Artista Digital": "Cria imagens, animações e artes digitais.",
    "Profissional de Marketing / Comunicação": "Gerencia campanhas, conteúdo e estratégias de comunicação.",
    "Designer de Experiência": "Cria interfaces intuitivas e centradas no usuário.",
    "Game Designer": "Desenvolve regras, histórias e mecânicas para jogos.",
    "Programador de CLP": "Atua na programação de controladores lógicos industriais.",
    "Analista Digital": "Trabalha com métricas digitais e otimização de campanhas.",
    "Arquiteto de Infraestrutura": "Planeja e mantém infraestrutura de TI, servidores e redes.",
    "Analista de Produto": "Auxilia no desenvolvimento e decisão estratégica do produto.",
    "Produtor de Conteúdo Digital": "Cria vídeos, posts, roteiros e conteúdo multimídia.",
    "DevOps": "Integra desenvolvimento e operações para entregar software rápido e seguro.",
    "Gerente de Produto de Marketing": "Coordena campanhas e projetos estratégicos de marketing.",
    "Engenheiro de IA": "Desenvolve modelos de inteligência artificial e automação inteligente.",
    "Engenheiro de Inovação": "Cria soluções inovadoras e aplica tecnologias emergentes.",
    "Desenvolvedor de Games": "Programa jogos digitais e participa da criação técnica.",
    "Líder de Inovação": "Coordena projetos inovadores e impulsiona transformação digital.",
    "Sem recomendação!": "Perfil não combina com carreiras mapeadas."
}    


class Model:
    def __init__(self, pessoa: Perfil, stage: str = "novo"):
        self.pessoa = pessoa
        self.stage = stage
        self.created = date.today().isoformat()

    def to_dict(self):
        return {
            "name": self.pessoa.nome,
            "email": self.pessoa.email,
            "stage": self.stage,
            "created": self.created,
            "perfil_type": self.pessoa.area(),
            "interesse": getattr(self.pessoa, "interesse", None)
        }

    def exibir_informacoes(self):
        return (
            f"{self.pessoa.exibir_informacoes()} | "
            f"Etapa: {self.stage} | Área: {self.pessoa.area()}"
        )

