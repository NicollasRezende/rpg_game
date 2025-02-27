
---

# RPG Game 2D

Este projeto é um jogo RPG em 2D feito com **Pygame**, inspirado em jogos como **Zelda**, onde o jogador pode explorar um mundo aberto, coletar itens, lutar contra inimigos, completar missões e melhorar seu personagem. O jogo segue uma arquitetura modular, permitindo fácil expansão e manutenção.

## Arquitetura do Projeto

O código foi organizado em diferentes módulos e pastas para garantir uma estrutura limpa, escalável e de fácil manutenção. Abaixo está uma descrição de cada parte do projeto:

### Estrutura de Pastas

```
/rpg_game
│── /assets          # Sprites, sons e mapas
│── /config          # Configurações do jogo (ex: resolução, FPS, etc.)
│── /core            # Engine principal (game loop, eventos, renderização)
│── /entities        # Classes para personagens, NPCs, inimigos e itens
│── /scenes          # Gerenciador de cenas (menu, jogo, inventário)
│── /systems         # Mecânicas (combate, inventário, quests, crafting)
│── main.py          # Ponto de entrada do jogo
│── settings.py      # Configurações globais
│── utils.py         # Funções auxiliares
```

### Descrição dos Componentes

#### `/assets`
Essa pasta contém todos os arquivos de mídia utilizados no jogo, como imagens (sprites), sons e mapas. Exemplos:
- **grass.png**: imagem do fundo do jogo.
- **player.png**: sprite do personagem do jogador.
- **enemy.png**: sprite dos inimigos.

#### `/config`
Contém configurações globais para o jogo, como:
- **Resolução da tela**.
- **FPS** (frames por segundo).
- **Outras configurações de gameplay** que podem ser ajustadas facilmente.

#### `/core`
Responsável pela lógica central do jogo, incluindo:
- **Game Loop**: A função principal de execução do jogo.
- **Eventos**: Processamento de entrada de teclado, mouse e outros dispositivos.
- **Renderização**: Desenha todos os objetos do jogo na tela.
- **Câmera**: Sistema de câmera para movimentação do jogador no mapa.

**Exemplo**:
- **camera.py**: Contém a lógica de movimentação da câmera, fazendo com que ela siga o jogador de forma suave e aplicando os offsets necessários.
- **background.py**: Responsável por carregar e desenhar o fundo do jogo (com texturas de tiles como grama, por exemplo).

#### `/entities`
Contém as classes para todas as entidades no jogo, como jogadores, NPCs, inimigos e objetos interativos. Cada entidade é responsável por:
- **Posição**: Onde ela está no mapa.
- **Movimento**: Como se move ou interage.
- **Renderização**: Como ela é desenhada na tela.

**Exemplo**:
- **player.py**: A classe do personagem jogável. Inclui a lógica de movimentação, colisões e interações com o ambiente.
- **enemy.py**: A classe dos inimigos. Inclui comportamentos simples de IA e colisões com o jogador.

#### `/scenes`
Contém as diferentes "cenas" ou telas do jogo. Cada cena tem um ciclo de vida próprio, com métodos para atualizar a lógica do jogo e renderizar a tela. O jogo pode ter várias cenas, como:
- **Menu Principal**: Onde o jogador inicia o jogo ou acessa as configurações.
- **Tela de Jogo**: Onde o jogador explora o mundo e interage com NPCs.
- **Inventário**: Onde o jogador vê e gerencia seus itens.

**Exemplo**:
- **game_scene.py**: A cena principal do jogo, onde o jogador interage com o mundo, completa missões e explora o ambiente.
- **menu_scene.py**: A cena onde o jogador pode iniciar o jogo ou acessar outras opções.

#### `/systems`
Contém a implementação das mecânicas do jogo, como:
- **Sistema de combate**: Lógica para o combate entre o jogador e inimigos.
- **Inventário**: Sistema para gerenciar itens que o jogador coleta e usa.
- **Quests**: Sistema de missões que o jogador pode aceitar e completar.

**Exemplo**:
- **combat.py**: Contém a lógica de combate do jogador (ataques, magias) e como o inimigo reage.
- **inventory.py**: Sistema de gerenciamento de itens coletados, usados ou equipados pelo jogador.

#### `main.py`
Ponto de entrada do jogo. Inicializa o jogo, cria a janela, inicia o game loop e troca entre as cenas. Carrega configurações iniciais e mantém o jogo rodando.

#### `settings.py`
Arquivo de configurações globais para o jogo, como:
- **SCREEN_WIDTH** e **SCREEN_HEIGHT**: Tamanho da tela.
- **FPS**: Frames por segundo.
- Outras configurações de gameplay que são usadas em várias partes do jogo.

#### `utils.py`
Funções auxiliares que são usadas em várias partes do código. Por exemplo:
- Funções para verificar colisões.
- Funções de inicialização para carregar imagens ou sons.
  
---

## Mecânicas do Jogo

### Movimentação do Jogador
A movimentação do jogador é controlada pelas teclas **WASD** e a física básica de colisões impede que o jogador se mova através de obstáculos.

### Sistema de Combate
O jogador pode atacar inimigos, coletar itens e melhorar suas habilidades ao longo do jogo.

### Quests e NPCs
O jogo inclui um sistema básico de quests. O jogador pode interagir com NPCs para receber tarefas e recompensas.

### Câmera
A câmera segue o jogador à medida que ele se move pelo mundo. A tela é limitada ao tamanho da tela de exibição e o resto do mundo é mostrado conforme o jogador avança.

---

## Como Rodar o Jogo

### Requisitos
- Python 3.8 ou superior.
- Pygame 2.0 ou superior.

### Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/rpg_game.git
    cd rpg_game
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute o jogo:
    ```bash
    python main.py
    ```

---

## Melhorias Futuras

1. **Animações de Personagem**: Adicionar animações para o movimento do jogador, ataques e magias.
2. **Sistema de Progressão do Personagem**: Implementar um sistema de experiência e aumento de atributos (força, agilidade, etc.).
3. **Mais Questões e Missões**: Aumentar o número de missões principais e secundárias, com enredo mais profundo.
4. **Aprimorar IA de Inimigos**: Criar inimigos com comportamentos mais avançados e reações ao jogador.
5. **Sistemas de Crafting e Economia**: Adicionar um sistema de crafting de itens e um mercado de economia no jogo.

---
