{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 910
        },
        "id": "MQZKI327KRDI",
        "outputId": "0c47f306-e8ff-41bf-bced-0dbcaa55731e"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "error",
          "ename": "ValueError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-20-1ed22113117e>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     32\u001b[0m \u001b[0mclustered_results\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     33\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 34\u001b[0;31m plt.scatter(Frames[clustered_results == 0], Frames[clustered_results == 1], \n\u001b[0m\u001b[1;32m     35\u001b[0m             s = 100, c = 'red', label = 'Iris-setosa')\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/matplotlib/pyplot.py\u001b[0m in \u001b[0;36mscatter\u001b[0;34m(x, y, s, c, marker, cmap, norm, vmin, vmax, alpha, linewidths, verts, edgecolors, plotnonfinite, data, **kwargs)\u001b[0m\n\u001b[1;32m   2809\u001b[0m         \u001b[0mverts\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcbook\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdeprecation\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_deprecated_parameter\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2810\u001b[0m         edgecolors=None, *, plotnonfinite=False, data=None, **kwargs):\n\u001b[0;32m-> 2811\u001b[0;31m     __ret = gca().scatter(\n\u001b[0m\u001b[1;32m   2812\u001b[0m         \u001b[0mx\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0ms\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mc\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mc\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmarker\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mmarker\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcmap\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcmap\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnorm\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mnorm\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2813\u001b[0m         \u001b[0mvmin\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mvmin\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvmax\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mvmax\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malpha\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0malpha\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlinewidths\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mlinewidths\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/matplotlib/__init__.py\u001b[0m in \u001b[0;36minner\u001b[0;34m(ax, data, *args, **kwargs)\u001b[0m\n\u001b[1;32m   1563\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0minner\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0max\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1564\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mdata\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1565\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0max\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0mmap\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msanitize_sequence\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1566\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1567\u001b[0m         \u001b[0mbound\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnew_sig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0max\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/matplotlib/cbook/deprecation.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    356\u001b[0m                 \u001b[0;34mf\"%(removal)s.  If any parameter follows {name!r}, they \"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    357\u001b[0m                 f\"should be pass as keyword, not positionally.\")\n\u001b[0;32m--> 358\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    359\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    360\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mwrapper\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/matplotlib/axes/_axes.py\u001b[0m in \u001b[0;36mscatter\u001b[0;34m(self, x, y, s, c, marker, cmap, norm, vmin, vmax, alpha, linewidths, verts, edgecolors, plotnonfinite, **kwargs)\u001b[0m\n\u001b[1;32m   4389\u001b[0m         \u001b[0my\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mma\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mravel\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0my\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4390\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msize\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msize\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 4391\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"x and y must be the same size\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   4392\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4393\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0ms\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mValueError\u001b[0m: x and y must be the same size"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "source": [
        "import pandas as pd\n",
        "from sklearn.cluster import KMeans\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "\n",
        "data = pd.read_csv('./Iris.csv')\n",
        "data.head()\n",
        "\n",
        "Frames = data.iloc[:, 1:4]\n",
        "distances = []\n",
        "for i in range(1,10):\n",
        "  kmeans = KMeans(n_clusters=i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)\n",
        "  kmeans.fit(Frames)\n",
        "  distances.append(kmeans.inertia_)\n",
        "\n",
        "#Plotting the Elbow curve\n",
        "plt.plot(range(1,10), distances)\n",
        "plt.xlabel('Cluster Numbers')\n",
        "plt.ylabel('Sum of Distances')\n",
        "plt.title('Elbow Curve Plot')\n",
        "plt.show()\n",
        "\n",
        "# We find the optimum cluster to be 3\n",
        "\n",
        "\n",
        "#Clustering \n",
        "means = KMeans(n_clusters = 3)\n",
        "means.fit(Frames)\n",
        "\n",
        "#Clusterng the Results\n",
        "clustered_results = means.fit_predict(Frames)\n",
        "clustered_results\n",
        "\n",
        "plt.scatter(Frames[clustered_results == 0], Frames[clustered_results == 1], \n",
        "            s = 100, c = 'red', label = 'Iris-setosa')\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "MvMGKU5TMjuj"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}