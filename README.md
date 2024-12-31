# Schedule2calendar
You may find English version below.

这个小工具可以整理把Timetable里面的信息，并产生一个ics文件。通过这个文件，我们可以快速地将整个学期的课程表导入iOS或者outlook的日历中。\n

相比通过链接订阅的方法，这份日历完全位于本地，不会因为跨时区导致时间不准。同时，这个工具支持自定义事件的标题，既可以选择使用课程代码表示（例如 PMGT0000 ），也可以直接显示课程名字。\n

由于中国大陆的坐标系存在加密和偏移，经过几次测试，位置信息不能很好的在日历中显示，所以当前版本没有在ics文件中加入日历信息，所以在导入日历时，需要手动添加一次位置。\n

## 功能概述
1. 支持两种规范：
    - outlook. 通过`4outlook.py`可以将csv数据转换成符合outlook规范的ics文件。
    - iOS. 通过`4iOS.py`可以将csv数据转换成符合苹果日历的ics文件。

2. CSV模板文件。提供了`schedule.csv`模板文件，在选课时打开Timeline网站，选择列表视图，并将课程信息直接复制到csv中即可。

3. 生成的ICS文件。ics文件可以直接导入outlook客户端或者Apple任意平台的日历软件，并通过iCloud全平台同步，后续支持在日历中直接修改。

## 更新列表

1. 添加教室位置。iOS日历可以根据日程发生的位置和当前自己的位置计算通勤时间，并在需要出发的时候通过iPhone提醒。目前，因为地址标准化的问题，添加的地址无法在iOS正确的显示，需要用户在导入后自行添加位置。

---

This tool can organize the information in Timetable and generate an ics file. With this file, we can quickly import the entire semester's course schedule into the iOS or Outlook calendar. \n

Compared to the method of subscribing through a link, this calendar is completely local and will not be inaccurate due to cross-time zone. At the same time, this tool supports custom event titles, which can be expressed by course codes (such as PMGT0000) or directly display course names. \n

Due to the encryption and offset of the coordinate system in mainland China, after several tests, the location information cannot be displayed well in the calendar, so the current version does not add calendar information to the ics file, so when importing the calendar, you need to manually add the location once. \n

## Function Overview
1. Support two specifications:
- Outlook. Through `4outlook.py`, csv data can be converted into ics files that comply with outlook specifications.
- iOS. Through `4iOS.py`, csv data can be converted into ics files that comply with Apple Calendar.

2. CSV template file. A `schedule.csv` template file is provided. When selecting courses, open the Timeline website, select the list view, and copy the course information directly into the csv file.

3. Generate ICS file. The ics file can be directly imported into the outlook client or the calendar software of any Apple platform, and synchronized through iCloud across all platforms. It can be modified directly in the calendar later.

## Update list

1. Add classroom location. The iOS calendar can calculate the commuting time based on the location of the schedule and the current location, and remind you through the iPhone when you need to leave. At present, due to the problem of address standardization, the added address cannot be displayed correctly on iOS, and users need to add the location themselves after importing.
