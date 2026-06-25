# template/ — onde você trabalha (Aula 4)

Aqui o sistema **já está com OCP**: cada tipo de ingresso é uma classe
(`modelos/ingresso.py`) e o serviço (`servico/bilheteria.py`) não tem mais
`if/elif`. Sua tarefa é **estender** essa hierarquia.

```
template/
├── modelos/ingresso.py     ← a hierarquia: Ingresso, Inteira, Meia, VIP
├── servico/bilheteria.py   ← total() polimórfico (sem if/elif)
└── main.py                 ← monta a venda e mostra o total
```

| O que você faz | Onde | Vale |
|---|---|---|
| adicionar a classe `Cortesia` (preço 0,00) à hierarquia | `modelos/ingresso.py` | 0,3 |
| incluir um `Cortesia()` na venda do `main.py` | `main.py` | — |

**Como rodar** (no terminal do Codespaces):
```bash
cd aula04/template
python main.py
```

**Como saber que está certo:**
- Antes de adicionar `Cortesia`: `Total: R$65.00`
- Depois (com `Cortesia()` na venda): ainda `R$65.00` — e você **não tocou** no `total()`
- Zero `if/elif` por tipo — se você precisou de um `if tipo == ...`, a tarefa não terminou

Passo a passo detalhado está no **roteiro da atividade** (SIGAA).
