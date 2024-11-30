---
title: "DQL, JS и встроенные функции"
source: "https://blacksmithgu.github.io/obsidian-dataview/queries/dql-js-inline/"
author:
published:
created: 2024-11-30
description:
tags:
  - "dataview"
  - "dql"
  - "js"
  - "function"
---
После того, как вы добавили [полезные данные на соответствующие страницы](https://blacksmithgu.github.io/obsidian-dataview/annotation/add-metadata/) , вы захотите отобразить их где-то или работать с ними. Dataview позволяет это сделать четырьмя различными способами, все из которых записываются в кодовые блоки непосредственно в вашем Markdown и перезагружаются в реальном времени при изменении вашего хранилища.

## Язык запросов к данным (DQL)

Язык [**запросов Dataview**](https://blacksmithgu.github.io/obsidian-dataview/queries/structure) (сокращенно **DQL** ) — это язык, подобный SQL, и основная функциональность Dataviews. Он поддерживает [четыре типа запросов](https://blacksmithgu.github.io/obsidian-dataview/queries/query-types/) для создания различных выходов, [команды данных](https://blacksmithgu.github.io/obsidian-dataview/queries/data-commands/) для уточнения, сортировки или группировки результатов и [многочисленные функции](https://blacksmithgu.github.io/obsidian-dataview/reference/functions/) , которые позволяют выполнять многочисленные операции и корректировки для достижения желаемого результата.

Вы создаете **DQL** -запрос с блоком кода, который использует `dataview`тип:

```
\`\`\`dataview
TABLE rating AS "Rating", summary AS "Summary" FROM #games
SORT rating DESC
\`\`\`
```

Используйте обратные кавычки

В допустимом блоке кода необходимо использовать обратные кавычки (\`) в начале и конце (по три в каждом). Не путайте обратные кавычки с похожим апострофом '!

Найдите объяснение, как написать DQL-запрос, в [справочнике по языку запросов](https://blacksmithgu.github.io/obsidian-dataview/queries/structure) . Если вы лучше усваиваете материал на примерах, взгляните на [примеры запросов](https://blacksmithgu.github.io/obsidian-dataview/resources/examples) .

## Встроенный DQL

Встроенный DQL использует формат встроенного блока вместо блока кода и настраиваемый префикс, чтобы обозначить этот встроенный блок кода как блок DQL.

Изменение префикса DQL

Вы можете изменить `=`токен на другой (например `dv:`, или `~`) в настройках Dataviews в разделе «Настройки Codeblock» > «Префикс встроенного запроса».

Встроенные запросы DQL отображают **ровно одно значение** где-то в середине заметки. Они органично вписываются в содержимое заметки:

```
Today is \`= date(today)\` - \`= [[exams]].deadline - date(today)\` until exams!
```

например, оказало бы

```
Today is November 07, 2022 - 2 months, 5 days until exams!
```

**Встроенный DQL** не может запрашивать несколько страниц. Они всегда отображают только одно значение, а не список (или таблицу) значений. Вы можете получить доступ к свойствам текущей **страницы** через префикс `this.`или к другой странице через `[[linkToPage]]`.

```
\`= this.file.name\`
\`= this.file.mtime\`
\`= this.someMetadataField\`
\`= [[secondPage]].file.name\`
\`= [[secondPage]].file.mtime\`
\`= [[secondPage]].someMetadataField\`
```

Вы можете использовать все, что доступно в качестве [выражений](https://blacksmithgu.github.io/obsidian-dataview/reference/expressions) и [литералов](https://blacksmithgu.github.io/obsidian-dataview/reference/literals) во встроенном запросе DQL, включая [функции](https://blacksmithgu.github.io/obsidian-dataview/reference/functions) . Типы запросов и команды данных, с другой стороны, **недоступны во встроенных запросах.**

```
Assignment due in \`= this.due - date(today)\`
Final paper due in \`= [[Computer Science Theory]].due - date(today)\`

🏃‍♂️ Goal reached? \`= choice(this.steps > 10000, "YES!", "**No**, get moving!")\`

You have \`= length(filter(link(dateformat(date(today), "yyyy-MM-dd")).file.tasks, (t) => !t.completed))\` tasks to do. \`= choice(date(today).weekday > 5, "Take it easy!", "Time to get work done!")\` 
```

## Просмотр данных JS

Dataview [JavaScript API](https://blacksmithgu.github.io/obsidian-dataview/api/intro) дает вам полную мощь JavaScript и предоставляет DSL для извлечения данных Dataview и выполнения запросов, позволяя вам создавать произвольно сложные запросы и представления. Подобно языку запросов, вы создаете блоки Dataview JS с помощью `dataviewjs`\-аннотированного блока кода:

```
\`\`\`dataviewjs
let pages = dv.pages("#books and -#books/finished").where(b => b.rating >= 7);
for (let group of pages.groupBy(b => b.genre)) {
   dv.header(3, group.key);
   dv.list(group.rows.file.name);
}
\`\`\`
```

Внутри блока JS dataview у вас есть доступ к полному API dataview через `dv`переменную. Для объяснения того, что вы можете с ней сделать, см. [документацию API](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference) или [примеры API](https://blacksmithgu.github.io/obsidian-dataview/api/code-examples) .

Расширенное использование

Написание запросов Javascript — это сложная техника, требующая понимания программирования и JS. Пожалуйста, имейте в виду, что запросы JS имеют доступ к вашей файловой системе, и будьте осторожны при использовании запросов JS других людей, особенно если они не опубликованы в сообществе Obsidian.

## Встроенный просмотр данных JS

Подобно языку запросов, вы можете писать встроенные запросы JS, которые позволяют вам напрямую встраивать вычисленное значение JS. Вы создаете встроенные запросы JS с помощью встроенных блоков кода:

```
\`$= dv.current().file.mtime\`
```

В inline DataviewJS у вас есть доступ к `dv`переменной, как в `dataviewjs`codeblocks, и вы можете делать все те же вызовы. Результатом должно быть что-то, что оценивается как значение JavaScript, которое Dataview автоматически отобразит соответствующим образом.

В отличие от встроенных запросов DQL, встроенные запросы JS имеют доступ ко всему, что доступно запросу Dataview JS, и, следовательно, могут запрашивать и выводить несколько страниц.

Изменение префикса Inline JS

Вы можете изменить `$=`токен на другой (например `dvjs:`, или `$~`) в настройках Dataviews в разделе «Настройки Codeblock» > «Префикс встроенного запроса Javascript».

Мы перевели эту страницу на Русский

Включить Английский обратно

Всегда переводить Английский на Русский  
Никогда не переводить Английский  
Никогда не переводить blacksmithgu.github.io