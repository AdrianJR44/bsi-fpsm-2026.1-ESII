# Aula 4 — OCP: Aberto para Extensão, Fechado para Modificação

Sistema da aula: **Bilheteria CineForma** — uma bilheteria que vende ingressos
e calcula o total da venda. O código já vem **em camadas** (como você aprendeu
nas Aulas 2 e 3), mas o serviço ainda decide o preço por tipo com `if/elif` — e
o **mesmo cálculo se repete em dois lugares**. Sua missão é aplicar **OCP**:
trocar o `if/elif` por uma classe para cada tipo, e adicionar um tipo novo sem
editar o código que já existe.

## O que tem aqui
```
aula04/
├── servico/bilheteria.py   ← o sistema v1.0 para ESTUDAR (vender/total com if/elif)
├── main.py                 ← ponto de entrada (roda o sistema)
└── template/               ← onde você TRABALHA e ENTREGA (já com OCP)
```

## Como começar
1. Leia os **slides da aula** (no SIGAA).
2. Rode o sistema atual para conhecê-lo:
   ```bash
   cd aula04
   python main.py
   ```
3. Faça a atividade dentro de `template/` (veja `template/README.md`).
4. `git push` e cole o **link do seu repositório** no SIGAA.
