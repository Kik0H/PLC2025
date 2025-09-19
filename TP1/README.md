# TPC1
**AUTOR: Francisco Bonjardim Dias, A108561**

Este TPC consiste em criar uma expressão regular que represente strings binários que não incluem a subsequência **"011"**. 

Depois de alguma pesquisa teórica e alguns [testes no regex](testes_regex.png), obtive a [expressão pretendida](expressao.txt).

```^1*0*(0|1)(0|01)*$```
