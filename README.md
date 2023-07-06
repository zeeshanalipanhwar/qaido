# Qaido
Qaido is a Large-Scale Font-Diverse Sindhi Ligature Recognition benchmark dataset. It is a collection of synthesized 22,597 Sindhi ligatures in 256 different Sindhi fonts. In total it comprises of 5,784,832 images which are randomly split into train and test sets with ratio 75:25 based on font styles. There are also some mini-versions of the data based on the lengths of ligatures, or their frequencies.

The following image contains five random Sindhi Ligatures in 14 random fonts.
![](doc/img/sprite_sindhi.png)

## Contents
 1. [Sindhi Script](#Sindhi-Script)
 2. [The Data](#the-data)
 3. [Tutorials](#Tutorials)
 4. [Pre-trained Models](#Using-the-pretrained-model)

### Sindhi Script
The Persian alphabet is a modification of the Arabic alphabet with four additional letters. It became the basis of Sindhi alphabet with two digraphs and eighteen new letters. The Sindhi alphabet has 52 letters, which is twice the number of letters in English, and covering wide varieties of sounds. The following figure shows the extended Perso-Arabic Sindhi script that is read from right to left.

<img src="doc/img/sindhi_alphabet.png" width="500" height="300" />

### The Data
A collection of ![104,145 unique words](data/sindhi_words.txt) has been extracted from four different sources, ![Shah Jo Risalo](https://github.com/amarfayazburiro/shah-sachal-sindhi-language/blob/master/Risalo(without-airab).txt), ![Sachal Jo Sindhi Kalaam](https://github.com/amarfayazburiro/shah-sachal-sindhi-language/blob/master/Corpus.txt), ![Quran Jo Tarjumo](https://github.com/zeeshanalipanhwar/quran-jo-tarjumo), and ![Digital South Asia Library](https://dsal.uchicago.edu/about.html). A total of ![22,597 Sindhi ligatures](data/ligatures.txt) are extracted from the collection of the words.
