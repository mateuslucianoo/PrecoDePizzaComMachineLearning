Preço de Pizza com Machine Learning

Este projeto tem como objetivo prever o preço de uma pizza com base no seu diâmetro. A ideia é mostrar, de forma prática e didática, como o aprendizado de máquina pode ser aplicado em situações simples do cotidiano. O modelo que calcula o preço foi feito usando regressão linear, um dos algoritmos mais básicos e fáceis de entender dentro do universo de machine learning.

Para desenvolver essa aplicação, usei as seguintes ferramentas:

Python: linguagem principal do projeto, usada tanto para o modelo quanto para a parte da interface.

Pandas: para leitura e manipulação dos dados da pizza (diâmetro e preço).

Scikit-learn: biblioteca usada para treinar o modelo de regressão linear.

Streamlit: framework que permite criar interfaces web de forma rápida e simples, sem precisar saber front-end. Ele transforma scripts Python em aplicações interativas com poucos comandos.

Basicamente, o usuário insere o diâmetro da pizza na interface e o modelo retorna o preço previsto, com base nos dados usados durante o treinamento.

Como rodar o projeto
Primeiro, clone o repositório:
git clone https://github.com/mateuslucianoo/PrecoDePizzaComMachineLearning.git
Acesse a pasta do projeto com:
cd PrecoDePizzaComMachineLearning

Crie um ambiente virtual para instalar os pacotes:
python -m venv .venv

Ative o ambiente virtual:

No Windows: .venv\Scripts\activate

No macOS ou Linux: source .venv/bin/activate

Instale as dependências do projeto com:
pip install -r requirements.txt

Rode a aplicação com o seguinte comando:
streamlit run testes/app.py

O navegador vai abrir automaticamente e você poderá testar a previsão de preço da pizza digitando o diâmetro.

Quer contribuir?
Se quiser melhorar algo ou sugerir uma nova funcionalidade, é só seguir os passos abaixo:

Faça um fork deste repositório no seu GitHub.

Crie uma nova branch:
git checkout -b minha-alteracao

Faça as alterações desejadas e salve:
git commit -m "Minha contribuição"

Suba suas mudanças para o seu repositório:
git push origin minha-alteracao

Depois, abra um Pull Request para que eu possa revisar.

Licença
Este projeto está sob a licença MIT, o que significa que você pode usar, copiar, modificar e distribuir à vontade. O conteúdo completo da licença está disponível no arquivo LICENSE.

Se quiser, posso te ajudar a colar esse texto no seu README.md também!
