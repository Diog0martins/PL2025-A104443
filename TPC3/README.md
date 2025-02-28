# Conversor de MarkDown para HTML

Este programa é capaz de converter elementos de MarkDown para elementos de HTML mantendo o mesmo conteúdo. Os elementos de MarkDown convertíveis são: 

- \*\*bold\*\*&nbsp;&nbsp;&nbsp;&nbsp;**->**&nbsp;&nbsp;&nbsp;&nbsp;\<b\>bold\</b\>
- \*italic\*&nbsp;&nbsp;&nbsp;&nbsp;**->**&nbsp;&nbsp;&nbsp;&nbsp;\<i\>italic\</i\>
- \## Header 2&nbsp;&nbsp;&nbsp;&nbsp;**->**&nbsp;&nbsp;&nbsp;&nbsp;\<h2\>Header 2\</h2\>
- Normal text&nbsp;&nbsp;&nbsp;&nbsp;**->**&nbsp;&nbsp;&nbsp;&nbsp;\<p\>Normal text\</p\>
- 1\. First item&nbsp;&nbsp;&nbsp;&nbsp;**->**&nbsp;&nbsp;&nbsp;&nbsp;\<ol\>\<li\>First item\</li\>\</ol\>
- \[Link\](http://example.com)&nbsp;&nbsp;&nbsp;&nbsp;**->**&nbsp;&nbsp;&nbsp;&nbsp;\<a href="http://example.com"\>Link\</a\>
- \![Image\](http://example.com/image.jpg)&nbsp;&nbsp;&nbsp;&nbsp;**->**&nbsp;&nbsp;&nbsp;&nbsp;\<img src="http://example.com/image.jpg" alt="Image"\>

Para realizar estas conversões no texto em MarkDown, foram usadas expressões regulares. Cada expressão regular foi capaz de fazer match com cada um destes componentes. As expressões regulares foram as seguintes: 

- **bold regex:**&nbsp;&nbsp;```\*\*(.*?)\*\*```
- **italic regex:**&nbsp;&nbsp;```\*(.*?)\*```
- **header regex**&nbsp;&nbsp;```(#+)(.+?)$```
- **paragraph regex:**&nbsp;&nbsp;```(?<=\n)(?!<)(?!\n)(.*)```
- **list regex:**&nbsp;&nbsp;```(\d+\..+?\n)+```
- **list element regex:**&nbsp;&nbsp;```^\d+\.(.+)$```
- **link regex:**&nbsp;&nbsp;```\[(.*?)\]\((.*?)\)```
- **image regex:**&nbsp;&nbsp;```!\[(.*?)\]\((.*?)\)```

Fazendo uso destas expressões regulares é possível substituir cada uma das respectivas ocorrências pelos elementos HTML correspondentes.

_**Nota:** O resultado da conversão é observável no stdout_
