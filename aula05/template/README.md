# template/ — onde voce trabalha (Aula 5)

O sistema **ja esta com DIP**: o servico recebe o repositorio e o enviador por
construtor (`servico/newsletter.py`), e ha uma interface `Enviador`
(`enviador/enviador.py`). Sua tarefa e a **prova de fogo do DIP**: criar um
**e-mail de mentira (fake)** e usa-lo no lugar do servidor real — provando que
da para testar **sem mandar e-mail de verdade**.

```
template/
├── modelos/assinante.py
├── repositorio/assinantes.py
├── enviador/enviador.py        ← Enviador (abstracao) + ServidorSMTP
├── servico/newsletter.py       ← recebe repo e email por construtor (pronto)
├── main.py                     ← monta tudo com o e-mail de verdade (pronto)
└── experimento.py              ← AQUI voce completa o FakeEmail
```

| O que voce faz | Onde | Vale |
|---|---|---|
| completar a classe `FakeEmail` (anota em vez de enviar) | `experimento.py` | 0,3 |

**Como rodar:**
```bash
cd aula05/template
python main.py          # o sistema real (imprime os envios do SMTP)
python experimento.py   # depois de completar o FakeEmail
```

**Como saber que esta certo:**
- `python experimento.py` imprime `Quem receberia: ['ana@exemplo.com', 'bia@exemplo.com']`
- nenhum e-mail e enviado de verdade — o FakeEmail so **anota** quem receberia
- voce **nao** mexeu no `servico/newsletter.py`: so injetou um enviador diferente

Passo a passo detalhado esta no **roteiro da atividade** (SIGAA).
