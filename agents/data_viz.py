import os
import matplotlib.pyplot as plt

class DataVizAgent:

    def make(self, topic, output_dir):

        path = os.path.join(output_dir, "chart.png")

        x = [1, 2, 3, 4, 5]
        y = [12, 18, 25, 31, 40]

        plt.figure(figsize=(7, 4))

        plt.plot(x, y, marker="o")

        plt.xlabel("Stage")
        plt.ylabel("Value")

        plt.title(f"Research Analysis: {topic}")

        plt.grid(True)

        plt.savefig(path, bbox_inches="tight")

        plt.close()

        return [path]