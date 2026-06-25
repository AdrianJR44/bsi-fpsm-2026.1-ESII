# Aula 5 — LSP, ISP e DIP

Sistema da aula: **Forma News** — uma newsletter que guarda assinantes e envia
cada edicao por e-mail. O sistema ja vem em camadas (servico, repositorio,
enviador, modelos), mas o **servico cria o repositorio e o servidor de e-mail
dentro de si** — e isso o torna **impossivel de testar** sem mandar e-mail de
verdade. Sua missao (na Parte B) e aplicar o **DIP**: fazer o servico **receber**
essas pecas por construtor, e usar um **fake** para testar sem e-mail real.

## O que tem aqui
```
aula05/
├── modelos/assinante.py        ← Assinante, Gratis, Premium (hierarquia p/ LSP)
├── repositorio/assinantes.py   ← guarda os assinantes (em memoria)
├── enviador/smtp.py            ← o e-mail "de verdade"
├── servico/newsletter.py       ← o servico v1.0 (CRIA as pecas dentro de si)
├── main.py                     ← roda o sistema
└── template/                   ← onde voce TRABALHA e ENTREGA (ja com DIP)
```

## Como comecar
1. Leia os **slides da aula** (no SIGAA).
2. Rode o sistema atual:
   ```bash
   cd aula05
   python main.py
   ```
3. Faca a atividade dentro de `template/` (veja `template/README.md`).
4. `git push` e cole o **link do seu repositorio** no SIGAA.
