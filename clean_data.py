{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOnVb6hwx6t/shJgHxlcYgj",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/fatimaalruhala/-Real-Estate-Analytics-Pipeline/blob/main/clean_data.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "np.random.seed(42)\n",
        "n_records = 10000\n",
        "\n",
        "data = {\n",
        "    'Listing_ID': [f'PROP_{i:05d}' for i in range(n_records)],\n",
        "    'Locality': np.random.choice(['Whitefield', 'Indiranagar', 'Koramangala', 'Electronic City', 'Jayanagar'], n_records),\n",
        "    'BHK_Raw': np.random.choice(['2 BHK', '3 BHK', '1 BHK', '4 BHK', None], n_records, p=[0.4, 0.3, 0.15, 0.1, 0.05]),\n",
        "    'Size_SqFt': np.random.randint(500, 4500, n_records),\n",
        "    'Price_Raw': np.random.choice(['₹ 75,00,000', '₹ 1,50,00,000', '₹ 45,00,000', 'Price On Request', '₹ 3,20,00,000'], n_records),\n",
        "    'Age_Years': np.random.randint(0, 20, n_records),\n",
        "    'Monthly_Rent_Raw': np.random.randint(15000, 95000, n_records)\n",
        "}\n",
        "\n",
        "df = pd.DataFrame(data)\n",
        "df.to_csv('raw_real_estate_listings.csv', index=False)\n",
        "print(\"Raw data generated successfully!\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KpEUp7s6E4N-",
        "outputId": "a5fbc1e3-9a0f-4ef5-b73d-910938dbc0c3"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Raw data generated successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "# 1. Load data\n",
        "df = pd.read_csv('raw_real_estate_listings.csv')\n",
        "\n",
        "# 2. Clean Price Column\n",
        "df['Price_Cleaned'] = df['Price_Raw'].str.replace('₹', '').str.replace(',', '').str.strip()\n",
        "df['Price_Cleaned'] = pd.to_numeric(df['Price_Cleaned'], errors='coerce')\n",
        "df['Price_Cleaned'] = df.groupby('Locality')['Price_Cleaned'].transform(lambda x: x.fillna(x.median()))\n",
        "\n",
        "# 3. Clean BHK Column\n",
        "df['BHK_Count'] = df['BHK_Raw'].str.extract(r'(\\d+)').astype(float)\n",
        "df['BHK_Count'] = df.groupby('Locality')['BHK_Count'].transform(lambda x: x.fillna(x.dropna().mode()[0] if not x.dropna().mode().empty else 2))\n",
        "\n",
        "# 4. Feature Engineering\n",
        "df = df[(df['Price_Cleaned'] > 1000000) & (df['Price_Cleaned'] < 500000000)]\n",
        "df['Price_Per_SqFt'] = df['Price_Cleaned'] / df['Size_SqFt']\n",
        "df['Annual_Rental_Yield'] = (df['Monthly_Rent_Raw'] * 12) / df['Price_Cleaned']\n",
        "\n",
        "# 5. Build Star Schema\n",
        "localities = df['Locality'].unique()\n",
        "dim_locality = pd.DataFrame({\n",
        "    'Locality_ID': [f'LOC_{i:03d}' for i in range(len(localities))],\n",
        "    'Locality_Name': localities,\n",
        "    'City': 'Bangalore'\n",
        "})\n",
        "\n",
        "df = df.merge(dim_locality, left_on='Locality', right_on='Locality_Name')\n",
        "fact_listings = df[['Listing_ID', 'Locality_ID', 'BHK_Count', 'Size_SqFt', 'Price_Cleaned', 'Price_Per_SqFt', 'Age_Years', 'Annual_Rental_Yield']]\n",
        "\n",
        "# 6. Export files\n",
        "dim_locality.to_csv('dim_locality.csv', index=False)\n",
        "fact_listings.to_csv('fact_listings.csv', index=False)\n",
        "print(\"Data schema built! Files are ready for download.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YNYbxcOHE-kt",
        "outputId": "eb97c6fb-5adb-44be-83d2-260b0681bb25"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Data schema built! Files are ready for download.\n"
          ]
        }
      ]
    }
  ]
}