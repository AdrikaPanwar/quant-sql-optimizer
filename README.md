# Quant-SQL Optimizer Project 🚀

### Overview 🧠
The **Quant-SQL Optimizer** is a cutting-edge project that explores the integration of **quantum computing** to optimize SQL queries using the logic behind **Grover's algorithm**. While quantum computing is still in its early stages, this project demonstrates the promising potential of quantum algorithms in real-world applications, particularly in SQL optimization. Built using **Qiskit**, IBM’s quantum computing framework, this project focuses on the algorithmic logic, bypassing some of the current limitations of quantum simulators like Qiskit Aer.

---

### Project Journey 🔍

The project was developed over the course of a month, exploring how quantum computing principles could interact with SQL query optimization. The results were both challenging and insightful. The core focus of this project was to show how **Grover's algorithm** can work for optimization purposes.

One of the key achievements of the project was its ability to optimize SQL queries based on uploaded datasets. However, there is a notable limitation in its current state:

- **Optimization Limitation**: When a dataset is uploaded, the optimizer transforms the SQL into a **single horizontal line**. While functional, this formatting makes the SQL query difficult to read and interpret, especially for more complex queries that are typically formatted vertically for readability.

- **Quantum Execution Challenges**: Due to issues with Qiskit Aer and the current limitations of quantum computing, the optimizer focuses on the theoretical logic of Grover's algorithm rather than full quantum execution.

Despite these challenges, the project successfully handles both small and large datasets, proving the concept of quantum-assisted optimization.

---

### Deployment Challenges 🚧

As a student developer, I faced several hurdles in deploying this project on common cloud platforms:

- **Heavy Library Requirements**: Due to the size and complexity of the Qiskit library and dependencies, I was unable to deploy this project on platforms like **Vercel** or **Heroku**.
- **Docker Limitations**: While Docker was explored as an alternative, Vercel’s limitations with larger Docker containers blocked this route as well.
- **Azure Subscription**: I used my free **Azure** subscription during development, but the cost of deploying such a heavy project on cloud services became prohibitive.

For these reasons, the project remains undeployed. However, a **video demonstration** is included in this repository, showcasing its functionality with both small and large datasets.

https://github.com/user-attachments/assets/c9bed227-ba03-45d3-aa34-31a9b5f58a55
---


### Current Status 📊

Although the project isn’t live, you can explore its logic and implementation:

- A **video demo** is attached to this repository to showcase how the project functions with different datasets.
- A **diagram** is also included to explain how **qubits** are leveraged in the optimization process.

The project is on hold for now, as I shift focus to other areas, but it still offers valuable insights into how quantum computing can be applied to SQL optimization.

---

### Future Plans 🔮

I plan to revisit this project once I expand my knowledge in **Machine Learning (ML)**, as ML could potentially enhance the capabilities of quantum algorithms in query optimization. At the moment, my priority is to work on projects related to my portfolio and job placements, but I remain enthusiastic about the future of quantum computing.

---

### How to Use This Repository 📂

This project is ideal for developers and researchers familiar with **quantum computing** and **Qiskit**:

- If you have experience with these technologies, this project offers a hands-on approach to quantum-powered SQL optimization.
- Before diving deep, make sure to check the **`requirements.txt`** file to understand the necessary libraries and dependencies.
- For those interested in contributing, feel free to fork the repository and submit pull requests. A deep understanding of quantum computing, Grover's algorithm, and Qiskit is recommended to contribute effectively.

---

### Contribution 🤝

I welcome contributions from anyone with knowledge of **quantum computing** and **Qiskit**. Your ideas and suggestions are valuable, and I encourage you to explore the code, run it locally, and help improve the project. If you're curious and willing to contribute, your input is highly appreciated!

---

### Final Thoughts ✨

I created the **Quant-SQL Optimizer** out of curiosity and a passion for exploring new technologies. While quantum computing is still in its infancy, this project is a small step toward realizing its potential in everyday applications like SQL optimization. 

Thank you for taking the time to explore this project. I hope you find it as exciting and insightful as I did while working on it. Feel free to contribute, share ideas, or just enjoy the journey into the world of **quantum computing**! 💡
