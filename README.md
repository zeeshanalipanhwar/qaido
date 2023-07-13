# Qaido
Qaido is a Large-Scale Font-Diverse Sindhi Ligature Recognition benchmark dataset. It is a collection of synthesized 22,597 Sindhi ligatures in 256 different Sindhi fonts. In total it comprises of 5,784,832 images which are randomly split into train and test sets with ratio 75:25 based on font styles. There are also some mini-versions of the data based on the lengths of ligatures, or their frequencies.

The following image contains five random Sindhi Ligatures in 14 random fonts.
![](doc/img/sprite_sindhi.png)

## Contents
 1. [Sindhi Script](#Sindhi-Script)
 2. [The Data](#the-data)
 3. [Tutorials](#Tutorials)
 4. [Pre-trained Models](#Pre-trained-models)

### Sindhi Script
The Persian alphabet is a modification of the Arabic alphabet with four additional letters. It became the basis of Sindhi alphabet with two digraphs and eighteen new letters. The Sindhi alphabet has 52 letters, which is twice the number of letters in English, and covering wide varieties of sounds. The following figure shows the extended Perso-Arabic Sindhi script that is read from right to left.

<img src="doc/img/sindhi_alphabet.png" width="500" height="300" />

### The Data
A collection of [104,145 unique words](data/sindhi_words.txt) has been extracted from four different sources, [Shah Jo Risalo](https://github.com/amarfayazburiro/shah-sachal-sindhi-language/blob/master/Risalo(without-airab).txt), [Sachal Jo Sindhi Kalaam](https://github.com/amarfayazburiro/shah-sachal-sindhi-language/blob/master/Corpus.txt), [Quran Jo Tarjumo](https://github.com/zeeshanalipanhwar/quran-jo-tarjumo), and [Digital South Asia Library](https://dsal.uchicago.edu/about.html). A total of [22,597 Sindhi ligatures](data/ligatures.txt) are extracted from the collection of the words. These ligatures are written on gray images of size $80\times80$ and labeled with the ligatures as classes. The following table contains all sets of synthetic data.

| Name  | Content | Classes | Examples | Size | Link | MD5 Checksum|
| --- | --- |--- | --- | --- |--- |--- |
| `train.tar.xz`        | training set images       | 22,597  | 4,338,624   | 2.65 GBytes   | [Download](https://drive.google.com/file/d/1hC0h_tnaL2AcuBiB6l-_NZTOvS4dFHXo/view?usp=sharing) |`c1df00bb2c8f3ca8f86981c173e11e60`|
| `test.tar.xz`         | test set images           | 22,597  | 1,446,208   | 905 MBytes    | [Download](https://drive.google.com/file/d/1EvM5SqDruOn1RBHf7vFk2ITS3sze90og/view?usp=sharing) |`393076c1f014a28d5bee285d4cb78b90`|
| `ligatures_map`       | index to ligature mapping | 22,597  | 22,597      | 219 KBytes    | [Download](https://drive.google.com/file/d/1LEjsDRrw-04oXeYLtsDIKUvLJVZNjhRh/view?usp=sharing) |`d5afa69dea351c1df16da7f785d4b42c`|
| `train1.tar.xz`       | training set images       | 55      | 10,560      | 4.1 MBytes    | [Download](https://drive.google.com/file/d/1yglPnEck2mMpFyobP5wsPjHknIiNpJ06/view?usp=sharing) |`7d18159f33de2caa0dfccf3c91b8549b`|
| `train2.tar.xz`       | training set images       | 1,119   | 214,848     | 116.5 MBytes  | [Download](https://drive.google.com/file/d/1oanftujv8CBFj9ezR5tQjH-MawvYsjpf/view?usp=sharing) |`86350c846d471b0de55b248f73a5be4f`|
| `train3.tar.xz`       | training set images       | 7,031   | 1,349,952   | 823.9 MBytes  | [Download](https://drive.google.com/file/d/1v0ofBdKj-HPIR3WohK9Rx-4e26bbzTju/view?usp=sharing) |`e05f2fa53547a453f026101ba18dfa0c`|
| `train4.tar.xz`       | training set images       | 16,472  | 1,349,952   | 1.94 GBytes   | [Download](https://drive.google.com/file/d/18uqBLOdJDxxgXA9MnmsJlmc35FBFBDYt/view?usp=sharing) |`1e4d0402347c47dfe40e850258278f7e`|
| `train_5000.tar.xz`   | training set images       | 5,000   | 960,000     | 581.9 MBytes  | [Download](https://drive.google.com/file/d/1BfMVm-L2ORngQCjpDDitTiyLylP5zImN/view?usp=sharing) |`c1db3f5e8c530499aaa9da7e9c731f38`|
| `test1.tar.xz`        | test set images           | 55      | 3,520       | 1.4 MBytes    | [Download](https://drive.google.com/file/d/1jUqVYGOJLeakr5wpNrL9dVT34MXnwAdF/view?usp=sharing) |`6e9c9ee73607da4201504566994b6e09`|
| `test2.tar.xz`        | test set images           | 1,119   | 7,616       | 38.7 MBytes   | [Download](https://drive.google.com/file/d/1gAT9jhqkYj2WNEbtR9iCAyBGkMd4zbxa/view?usp=sharing) |`79aa49ba9c1638847fdaf9c58990f7c8`|
| `test3.tar.xz`        | test set images           | 7,031   | 449,984     | 274.8 MBytes  | [Download](https://drive.google.com/file/d/1VIYlPKJI1EnFekOADswDpdVrhyhi9dWe/view?usp=sharing) |`4598e9a30cc989a9a4db7c17a76ac531`|
| `test4.tar.xz`        | test set images           | 16,472  | 1,054,208   | 662.5 MBytes  | [Download](https://drive.google.com/file/d/1euqfYVJdwmwwwYjvYCp8MoIenwN3ehI9/view?usp=sharing) |`b0df91021bb4d0c6396bb31a2e0c6517`|
| `test_5000.tar.xz`    | test set images           | 5,000   | 320,000     | 194.1 MBytes  | [Download](https://drive.google.com/file/d/1P0Y9yxH3ZRD1YQ0rYaLtccKMa_3L_1wH/view?usp=sharing) |`8bf0d00db37004ca01595f9133241b01`|
| `ligatures_map_5000`  | index to ligature mapping | 5,000   | 5,000       | 42 KBytes     | [Download](https://drive.google.com/file/d/1kwFWvmLloyDb7bLIq0stJEyq4KFh1ymP/view?usp=sharing) |`93cf0c3228e42addaca9774a5fe07c30`|

#### Data format
The training and test data sets are arranged in the following data structure:

```markdown
train
|
├── 0               // directory name is class index
│   ├── 0.png
│   ├── 1.png
│   └── ...
|
├── 1               
│   ├── 0.png
│   ├── 1.png
|   └─── ...
|
⋮
└── ...

```

#### Mapping directory/class to ligature 
Use the following code to map a class directory to its corresponding ligature.
 
```python
import codecs
with codecs.open('./data/ligatures_map', encoding='UTF-16LE') as ligature_file:
    ligatures_map = ligature_file.readlines()

class_idx = 22597
ligature = ligatures_map[class_idx]
print(ligature)

>>>  ‫ﺟﮭﻨﮕﻠﻴﭙﮣﻮ‬
``` 

### Tutorials
For tutorials and code, use those of Qaida from [here](https://github.com/AtiqueUrRehman/qaida/tree/master#Tutorials).

### Pre-trained Models
The following table shows the models and their performance on their respective test sets of 64 unseen fonts.
| Name  | Precision | Recall | Accuracy | $\mathbf{F_1-Score}$ | Size | Link | MD5 Checksum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SLRNet-22597` | 92.55% | 91.85% | 91.85% | 91.95% | 173.8 MBytes | [Download](https://drive.google.com/file/d/1-9YulWRPLeBmqS_SlsPNtLIDd1qEwY-K/view?usp=sharing) | `7df8624c80d9ebf2d04fb250c3be89bb` |
| `SLRNet-5000`  | _      | _      | 90.00% | _      | 105 MBytes   | [Download](https://drive.google.com/file/d/1-E_FE7FoHankNhZA6TK7TwBacbE45Vuo/view?usp=sharing) | `d73e1c98ae23b4c64c638aebb06fbb46` |

#### For a live demo of the SLRNet-22597 view [qaido](https://huggingface.co/spaces/ZeeshanAli/qaido) on HuggingFace spaces.

## License
This project is licensed under the terms of the [Creative Commons license](https://github.com/zeeshanalipanhwar/qaido/blob/master/LICENSE).

## Acknowledgements
This project structure followed guidlines from [Qaida](https://github.com/AtiqueUrRehman/qaida) repository.

## Author
`Maintainer` [Zeeshan Ali](https://github.com/zeeshanalipanhwar) (zapt1860@gmail.com)

