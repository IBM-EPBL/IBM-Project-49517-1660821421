{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": []
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
      "execution_count": null,
      "metadata": {
        "id": "bzqoCLZRGmVW"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import nltk\n",
        "import re"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Loading Dataset"
      ],
      "metadata": {
        "id": "cUdjBOGgG1_v"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data=pd.read_csv('/content/drive/MyDrive/IBM/spam.csv',encoding=\"ISO-8859-1\")"
      ],
      "metadata": {
        "id": "F8IEA9VuGsx0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Data Preprocessing**"
      ],
      "metadata": {
        "id": "KTdKSNxkHqTd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Encoding the categorical coulmn"
      ],
      "metadata": {
        "id": "fsATPL65H-i8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.preprocessing import LabelEncoder\n",
        "le=LabelEncoder()"
      ],
      "metadata": {
        "id": "aIAJjte1HUFb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data['v1']=le.fit_transform(data['v1'])"
      ],
      "metadata": {
        "id": "ChSwbL3kIg_R"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data.head(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 250
        },
        "id": "u4sWO1osI2Ps",
        "outputId": "896921e8-82bb-4aab-93eb-0485a205ceb7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   v1                                                 v2 Unnamed: 2  \\\n",
              "0   0  Go until jurong point, crazy.. Available only ...        NaN   \n",
              "1   0                      Ok lar... Joking wif u oni...        NaN   \n",
              "2   1  Free entry in 2 a wkly comp to win FA Cup fina...        NaN   \n",
              "3   0  U dun say so early hor... U c already then say...        NaN   \n",
              "4   0  Nah I don't think he goes to usf, he lives aro...        NaN   \n",
              "\n",
              "  Unnamed: 3 Unnamed: 4  \n",
              "0        NaN        NaN  \n",
              "1        NaN        NaN  \n",
              "2        NaN        NaN  \n",
              "3        NaN        NaN  \n",
              "4        NaN        NaN  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-856d9844-e30f-4f09-a5c3-8c660ae4d774\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>v1</th>\n",
              "      <th>v2</th>\n",
              "      <th>Unnamed: 2</th>\n",
              "      <th>Unnamed: 3</th>\n",
              "      <th>Unnamed: 4</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0</td>\n",
              "      <td>Ok lar... Joking wif u oni...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0</td>\n",
              "      <td>U dun say so early hor... U c already then say...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0</td>\n",
              "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-856d9844-e30f-4f09-a5c3-8c660ae4d774')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-856d9844-e30f-4f09-a5c3-8c660ae4d774 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-856d9844-e30f-4f09-a5c3-8c660ae4d774');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nltk.download('stopwords')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1pTHUx1LJDBs",
        "outputId": "562069f7-403d-43a6-a9dc-e1aa7b78ace3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package stopwords to /root/nltk_data...\n",
            "[nltk_data]   Unzipping corpora/stopwords.zip.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from nltk.corpus import stopwords\n",
        "from nltk.stem.porter import PorterStemmer "
      ],
      "metadata": {
        "id": "6zluDmS8JLXT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "pe=PorterStemmer()\n",
        "arr=[]"
      ],
      "metadata": {
        "id": "4wAdDYf5Jjze"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YR06yHboJyZL",
        "outputId": "704fe80a-1749-4cb0-ed00-6afb790440f0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(5572, 5)"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(5572):\n",
        "  msg=data['v2'][i]\n",
        "  msg=re.sub('[^a-zA-Z]',' ',msg)\n",
        "  msg=msg.lower()\n",
        "  msg=msg.split()\n",
        "  msg=[pe.stem(word) for word in msg if not word in set(stopwords.words('english'))]\n",
        "  msg=' '.join(msg)\n",
        "  arr.append(msg)"
      ],
      "metadata": {
        "id": "f_Be0EN4J1he"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.feature_extraction.text import CountVectorizer\n",
        "cv=CountVectorizer(max_features=10000)"
      ],
      "metadata": {
        "id": "AedJ4IDcK_0N"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "x=cv.fit_transform(arr).toarray()"
      ],
      "metadata": {
        "id": "9nbPgnJgLiY4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "x"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FLb8b5BlLqL_",
        "outputId": "0cfa6aaa-d206-4c3d-c6c6-c121c3dfb1af"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0],\n",
              "       ...,\n",
              "       [0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0]])"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tbRNp4ecL8b9",
        "outputId": "86a30e20-70e3-4402-af1a-0c12228d44e5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(5572, 6221)"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y=data['v1'].values"
      ],
      "metadata": {
        "id": "kiNZgulTMEtj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "y"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cwmSJu_pMKD1",
        "outputId": "82f23199-e29e-42f5-fb0f-788f1e5bea74"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([0, 0, 1, ..., 0, 0, 0])"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Train and Test Split"
      ],
      "metadata": {
        "id": "bSBdrIr3MNd8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split"
      ],
      "metadata": {
        "id": "XM2Z5-YCMLhq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)"
      ],
      "metadata": {
        "id": "inLgxftMMaQX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**MOdel building**"
      ],
      "metadata": {
        "id": "GXyM2evaMs6m"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from tensorflow.keras.models import Sequential\n",
        "from tensorflow.keras.layers import Dense"
      ],
      "metadata": {
        "id": "SSuu0dORMq-g"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model=Sequential()"
      ],
      "metadata": {
        "id": "DOufhDq1NQvG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.add(Dense(units=6221,activation='relu'))\n",
        "model.add(Dense(units=10000,activation='relu'))\n",
        "model.add(Dense(units=1,activation='sigmoid'))"
      ],
      "metadata": {
        "id": "ate33jzCNc7Y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])"
      ],
      "metadata": {
        "id": "q7YrvdnTN8bH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.fit(x_train,y_train,epochs=5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b482CWmSOmNH",
        "outputId": "32a5f734-1bd7-4700-f454-3de829aa4059"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/5\n",
            "140/140 [==============================] - 64s 441ms/step - loss: 0.1266 - accuracy: 0.9670\n",
            "Epoch 2/5\n",
            "140/140 [==============================] - 59s 424ms/step - loss: 0.0069 - accuracy: 0.9984\n",
            "Epoch 3/5\n",
            "140/140 [==============================] - 59s 424ms/step - loss: 8.1224e-04 - accuracy: 0.9998\n",
            "Epoch 4/5\n",
            "140/140 [==============================] - 61s 433ms/step - loss: 1.1299e-04 - accuracy: 1.0000\n",
            "Epoch 5/5\n",
            " 25/140 [====>.........................] - ETA: 49s - loss: 4.9234e-05 - accuracy: 1.0000"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Saving Model"
      ],
      "metadata": {
        "id": "ViuoCXGlQqmg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ls"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gGnKNkBVO4ui",
        "outputId": "737e157a-1f19-4576-aa61-66a3d5e7bf29"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[0m\u001b[01;34mdrive\u001b[0m/  \u001b[01;34msample_data\u001b[0m/\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cd /content/drive/MyDrive/IBM"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TMPLAIKxQupi",
        "outputId": "2fc4e99e-68a2-4c08-9bbf-6b7b32d64549"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/MyDrive/IBM\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model.save('spamDetector.h5')"
      ],
      "metadata": {
        "id": "UliVIvb2Q7mb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Testing Model"
      ],
      "metadata": {
        "id": "7IZyYdu1RKNT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from tensorflow.keras.models import load_model"
      ],
      "metadata": {
        "id": "76u7nRh0RGCX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model=load_model('/content/drive/MyDrive/IBM/spamDetector.h5')"
      ],
      "metadata": {
        "id": "tYlMY5alRWVz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def preprocessing(text):\n",
        "  text=re.sub('[^a-zA-Z]',' ',text)\n",
        "  text=text.lower()\n",
        "  text=text.split()\n",
        "  text=[pe.stem(word) for word in text if not word in set(stopwords.words('english'))]\n",
        "  text=' '.join(text)\n",
        "  return text"
      ],
      "metadata": {
        "id": "fYS08bGSRhN4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "message='WINNER!! As a valued network customer you have been selected to receivea ???900 prize reward! To claim call 09061701461. Claim code KL341. Valid 12 hours only.'"
      ],
      "metadata": {
        "id": "Itjf4dY5Sjfb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "message=preprocessing(message)"
      ],
      "metadata": {
        "id": "_sDnEOcBS-dq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "message"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        },
        "id": "Z7y77rkLTFq1",
        "outputId": "c839b864-1384-4300-a2d8-3c968f1df5b3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'winner valu network custom select receivea prize reward claim call claim code kl valid hour'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "result=model.predict(cv.transform([message]))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Im-UnvpTTHxV",
        "outputId": "97116efb-a6db-498f-c5da-03f80873d9c3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1/1 [==============================] - 0s 377ms/step\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "result"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f-Pvnb5oUAEg",
        "outputId": "d45f7585-6930-44a6-eac7-8ec74f6ad76d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1.]], dtype=float32)"
            ]
          },
          "metadata": {},
          "execution_count": 55
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if(result>0.5):\n",
        "  print(\"Spam Message!!!\")\n",
        "else:\n",
        "  print(\"Not Spam\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ARFcJUDDTSyx",
        "outputId": "b9a5aef4-7fdc-4b6e-a9ae-66917a30e87b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Spam Message!!!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "v0pt_OQQUWpa"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}