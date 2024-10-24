# Projeto Aplicado - Gerenciamento de Estoque com ESP32-CAM e Edge Impulse

Este projeto é um sistema automatizado para gerenciamento de estoque utilizando um ESP32-CAM com reconhecimento de objetos. O sistema é capaz de detectar produtos em tempo real e atualizar automaticamente um banco de dados local. A implementação utiliza a plataforma Edge Impulse para o treinamento de modelos de visão computacional, otimizando o processo de controle de inventário.

## Tecnologias Utilizadas
- ESP32-CAM: Microcontrolador com câmera embutida para captura de imagens e detecção de objetos.
- Edge Impulse: Plataforma para desenvolvimento e implementação de modelos de aprendizado de máquina.
- Python: Utilizada para interagir com o banco de dados e realizar atualizações de estoque.
- SQLite: Banco de dados utilizado para armazenar informações do estoque.

## Funcionalidades
- Interface Serial: Comunicação com o ESP32-CAM através da porta serial para monitoramento e controle.
- Detecção de Produtos: Utiliza visão computacional para identificar produtos em tempo real.
- Atualização de Estoque: O sistema desconta automaticamente os produtos detectados do estoque.
- Banco de Dados Local: Armazena informações de produtos e quantidades em um banco de dados SQLite.
