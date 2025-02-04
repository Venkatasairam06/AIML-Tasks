{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "462f04d7-130f-491e-971c-24f16418b2bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns \n",
    "import statsmodels.formula.api as smf\n",
    "from statsmodels.graphics.regressionplots import influence_plot\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "78a9b3eb-3f2a-40a6-91d6-206038d2d9f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>HP</th>\n",
       "      <th>MPG</th>\n",
       "      <th>VOL</th>\n",
       "      <th>SP</th>\n",
       "      <th>WT</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>49</td>\n",
       "      <td>53.700681</td>\n",
       "      <td>89</td>\n",
       "      <td>104.185353</td>\n",
       "      <td>28.762059</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>55</td>\n",
       "      <td>50.013401</td>\n",
       "      <td>92</td>\n",
       "      <td>105.461264</td>\n",
       "      <td>30.466833</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>55</td>\n",
       "      <td>50.013401</td>\n",
       "      <td>92</td>\n",
       "      <td>105.461264</td>\n",
       "      <td>30.193597</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>70</td>\n",
       "      <td>45.696322</td>\n",
       "      <td>92</td>\n",
       "      <td>113.461264</td>\n",
       "      <td>30.632114</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>53</td>\n",
       "      <td>50.504232</td>\n",
       "      <td>92</td>\n",
       "      <td>104.461264</td>\n",
       "      <td>29.889149</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   HP        MPG  VOL          SP         WT\n",
       "0  49  53.700681   89  104.185353  28.762059\n",
       "1  55  50.013401   92  105.461264  30.466833\n",
       "2  55  50.013401   92  105.461264  30.193597\n",
       "3  70  45.696322   92  113.461264  30.632114\n",
       "4  53  50.504232   92  104.461264  29.889149"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cars = pd.read_csv(\"Cars.csv\")\n",
    "cars.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3e8033ad-3762-42e8-af30-f188e3ed818b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>HP</th>\n",
       "      <th>VOL</th>\n",
       "      <th>SP</th>\n",
       "      <th>WT</th>\n",
       "      <th>MPG</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>49</td>\n",
       "      <td>89</td>\n",
       "      <td>104.185353</td>\n",
       "      <td>28.762059</td>\n",
       "      <td>53.700681</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>55</td>\n",
       "      <td>92</td>\n",
       "      <td>105.461264</td>\n",
       "      <td>30.466833</td>\n",
       "      <td>50.013401</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>55</td>\n",
       "      <td>92</td>\n",
       "      <td>105.461264</td>\n",
       "      <td>30.193597</td>\n",
       "      <td>50.013401</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>70</td>\n",
       "      <td>92</td>\n",
       "      <td>113.461264</td>\n",
       "      <td>30.632114</td>\n",
       "      <td>45.696322</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>53</td>\n",
       "      <td>92</td>\n",
       "      <td>104.461264</td>\n",
       "      <td>29.889149</td>\n",
       "      <td>50.504232</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   HP  VOL          SP         WT        MPG\n",
       "0  49   89  104.185353  28.762059  53.700681\n",
       "1  55   92  105.461264  30.466833  50.013401\n",
       "2  55   92  105.461264  30.193597  50.013401\n",
       "3  70   92  113.461264  30.632114  45.696322\n",
       "4  53   92  104.461264  29.889149  50.504232"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cars = pd.DataFrame(cars,columns=[\"HP\",\"VOL\",\"SP\",\"WT\",\"MPG\"])\n",
    "cars.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5c81d839-94d4-4210-9dec-7e8c91cb3176",
   "metadata": {},
   "source": [
    "#### Description of columns\n",
    "- MPG: Milege of the car(Mile per Gallon)(This is T-column to be predicted)\n",
    "- HP:Horse Power of the car(X1 column)\n",
    "- VOL:Volume of the car(size)(X2 column)\n",
    "- SP: Top speed of the car(Miles per Hour)(X3 column)\n",
    "- WT:Weight of the car(pounds)(X4 column)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb46c470-c66a-4984-af3e-d0b59a25aea4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:New folder]",
   "language": "python",
   "name": "conda-env-New_folder-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
