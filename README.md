# 🍕 Preço de Pizza com Machine Learning

Este projeto tem como objetivo prever o preço de uma pizza com base no seu diâmetro. A ideia é mostrar, de forma prática e didática, como o aprendizado de máquina pode ser aplicado em situações simples do cotidiano. O modelo que calcula o preço foi feito usando regressão linear, um dos algoritmos mais básicos e fáceis de entender dentro do universo de machine learning.

## 🛠️ Tecnologias utilizadas

Para desenvolver essa aplicação, usei as seguintes ferramentas:

- **🐍 Python**: linguagem principal do projeto, usada tanto para o modelo quanto para a parte da interface.  
- **📊 Pandas**: para leitura e manipulação dos dados da pizza (diâmetro e preço).  
- **📈 Scikit-learn**: biblioteca usada para treinar o modelo de regressão linear.  
- **🌐 Streamlit**: framework que permite criar interfaces web de forma rápida e simples, sem precisar saber front-end. Ele transforma scripts Python em aplicações interativas com poucos comandos.

Basicamente, o usuário insere o diâmetro da pizza na interface e o modelo retorna o preço previsto com base nos dados usados durante o treinamento.

---

## ▶️ Como rodar o projeto

1. Clone o repositório:  
   ```bash
   git clone https://github.com/mateuslucianoo/PrecoDePizzaComMachineLearning.git
   cd PrecoDePizzaComMachineLearning
   ```

2. Crie um ambiente virtual:  
   ```bash
   python -m venv .venv
   ```

3. Ative o ambiente virtual:  
   - No **Windows**:  
     ```
     .venv\Scripts\activate
     ```  
   - No **macOS/Linux**:  
     ```
     source .venv/bin/activate
     ```

4. Instale as dependências do projeto:  
   ```bash
   pip install -r requirements.txt
   ```

5. Rode a aplicação:  
   ```bash
   streamlit run testes/app.py
   ```

O navegador abrirá automaticamente e você poderá testar a previsão de preço da pizza digitando o diâmetro 🍕📏.

---

## 🤝 Quer contribuir?

Se quiser melhorar algo ou sugerir uma nova funcionalidade, é só seguir os passos abaixo:

1. Faça um **fork** deste repositório no seu GitHub.
2. Crie uma nova branch:  
   ```bash
   git checkout -b minha-alteracao
   ```
3. Faça as alterações desejadas e salve:  
   ```bash
   git commit -m "Minha contribuição"
   ```
4. Suba suas mudanças:  
   ```bash
   git push origin minha-alteracao
   ```
5. Abra um **Pull Request** para que eu possa revisar!

---

## 📄 Licença

Este projeto está sob a licença **MIT**, o que significa que você pode usar, copiar, modificar e distribuir à vontade. O conteúdo completo da licença está disponível no arquivo `LICENSE`.
