---
title: Разработка с использованием Dataview
description: Руководство по разработке с использованием Dataview, включая лучшие практики и советы
tags:
  - dataview
  - development
  - programming
  - documentation
  - best-practices
keywords:
  - разработка
  - dataview
  - программирование
  - лучшие практики
  - советы разработчикам
created: 2024-11-30
updated: 2024-12-15
category: Obsidian/Plugins/Dataview/Resources
source: https://blacksmithgu.github.io/obsidian-dataview/resources/development/
author: blacksmithgu
language: ru
черновик: false
статус: ✅ Готово
архив: false
---

Dataview включает в себя высокоуровневый API для работы с плагинами, а также определения TypeScript и библиотеку утилит. Чтобы установить его, просто используйте:

```
npm install -D obsidian-dataview
```

Чтобы убедиться, что установлена ​​правильная версия, выполните `npm list obsidian-dataview`. Если это не позволяет получить последнюю версию, которая в настоящее время является 0.5.64, вы можете выполнить:

```
npm install obsidian-dataview@0.5.64
```

**Примечание** : Если [Git](http://git-scm.com/) еще не установлен на вашей локальной системе, вам сначала нужно будет установить его. Возможно, вам придется перезапустить устройство, чтобы завершить установку Git, прежде чем вы сможете установить Dataview API.

##### Доступ к API Dataview

Эту функцию можно использовать `getAPI()`для получения API плагина Dataview; он возвращает `DataviewApi`объект, который предоставляет различные утилиты, включая рендеринг представлений данных, проверку версии представления данных, подключение к жизненному циклу событий представления данных и запрос метаданных представления данных.

```
import { getAPI } from "obsidian-dataview";

const api = getAPI();
```

Полные определения API можно найти в файле [index.ts](https://github.com/blacksmithgu/obsidian-dataview/blob/master/src/index.ts) или в определении API плагина plugin [\-api.ts](https://github.com/blacksmithgu/obsidian-dataview/blob/master/src/api/plugin-api.ts) .

##### Привязка к событиям Dataview

Вы можете выполнить привязку к событиям метаданных dataview, которые срабатывают при всех обновлениях и изменениях файлов, с помощью:

```
plugin.registerEvent(plugin.app.metadataCache.on("dataview:index-ready", () => {
    ...
});

plugin.registerEvent(plugin.app.metadataCache.on("dataview:metadata-change",
    (type, file, oldPath?) => { ... }));
```

Для всех событий, подключенных к MetadataCache, проверьте [index.ts](https://github.com/blacksmithgu/obsidian-dataview/blob/master/src/index.ts) .

##### Значение Утилиты

Вы можете получить доступ к различным утилитам, которые позволяют проверять типы объектов и сравнивать их с помощью `Values`:

```
import { getAPI, Values } from "obsidian-dataview";

const field = getAPI(plugin.app)?.page('sample.md').field;
if (!field) return;

if (Values.isHtml(field)) // do something
else if (Values.isLink(field)) // do something
// ...
