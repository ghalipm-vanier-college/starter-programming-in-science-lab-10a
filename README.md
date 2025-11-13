
##  **README.md**

# Programming in Science - Lab 10

This template repository is the starter project for **Programming in Science Lab 10**.  
Written in Python, and tested with **unittest**.

---

### Question(s)

#### **1️⃣ (25%) Plot a Mathematical Curve**

- Write a function `plot_curve()` that generates and plots a **mathematical curve** using NumPy and Matplotlib.  
- Use `np.linspace()` to generate evenly spaced x-values between -10 and 10, and compute corresponding y-values for the equation  
  \[
  y = x^2
  \]
- Display the graph with proper axis labels and title.

#### Example:
```python
plot_curve()  # Plots y = x^2 curve
````

✅ **Hints:**

* Use `np.linspace(-10, 10, 100)` for x-values.
* Use `plt.plot(x, y)` and `plt.show()`.

---

#### **2️⃣ (25%) Plot a Sine and Cosine Function**

* Write a function `plot_trig_functions()` that plots **sine and cosine** curves on the same graph.
* Use `np.arange()` from 0 to ( 2\pi ) with a small step.
* Label each curve clearly and add a legend.

#### Example:

```python
plot_trig_functions()  # Plots sin(x) and cos(x)
```

✅ **Hints:**

* Use `np.arange(0, 2 * np.pi, 0.1)` for x-values.
* Use `plt.plot(x, np.sin(x))` and `plt.plot(x, np.cos(x))`.

---

#### **3️⃣ (25%) Visualize Data from a `.txt` File using Pandas**

- Write a function `plot_temperature_data(filename)` that reads a `.txt` file containing two columns:  
  **Day** and **Temperature (°C)**, separated by spaces.  
- Plot the temperature variation across the days of the week.

#### Example file (`temperature.txt`):

✅ **Hints:**
* Use `pandas.read_csv(filename, sep=' ', header=None)` to read data.
* Use `plt.plot()` with labels and titles.
---

#### **4️⃣ (25%) Visualize Data from a `.csv` File using Pandas**

* Write a function `plot_population_data(filename)` that reads a `.csv` file containing two columns:
  **Year** and **Population**.
* Create a **scatter plot** of population over time.

#### Example file (`population.csv`):

```
Year,Population
2000,500
2005,700
2010,850
2015,950
2020,1200
```

#### Example:

```python
plot_population_data("population.csv")
```

✅ **Hints:**

* Use `pandas.read_csv()` to read the file.
* Use `plt.scatter()` for the plot.
* Add a grid and appropriate labels.

---

###  Run Command

To run the tests, use:

```bash
pytest
```
