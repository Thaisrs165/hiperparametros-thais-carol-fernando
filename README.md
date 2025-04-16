# hiperparametros-thais-carol-fernando

Alphas mais altos (como 0.80) aprendem mais rápido, mas podem oscilar.

Alphas mais baixos (como 0.10) são mais estáveis, porém lentos.

Alpha = 0.40 parece ser um bom equilíbrio, oferecendo uma convergência rápida com razoável estabilidade.

![alt text](<Screenshot 2025-04-15 at 21.29.44.png>)

γ = 0.40 parece ser o valor mais equilibrado, com boa performance tanto no curto quanto no longo prazo.

Valores muito altos (γ = 0.80) podem introduzir pequenas oscilações por priorizar demais recompensas futuras, o que pode ser desnecessário no TaxiDriver.

![alt text](<Screenshot 2025-04-15 at 21.29.56.png>)

Exploração total (ε = 1.0) é ruim: o agente não aprende nada útil a longo prazo.

Exploração controlada (ε = 0.1) foi a mais eficaz: o agente explora um pouco, mas rapidamente foca em boas ações.

Exploração com decaimento pode ser uma boa estratégia se bem calibrada, mas aqui ela ficou atrás da fixa.

![alt text](<Screenshot 2025-04-15 at 21.30.07.png>)
