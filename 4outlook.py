import csv
from datetime import datetime, timedelta


# 定义解析 Weeks 字段的函数
def parse_weeks(weeks_str, year):
    date_ranges = []
    for period in weeks_str.split(", "):
        start_str, end_str = period.split("-")
        start_date = datetime.strptime(f"{start_str}/{year}", "%d/%m/%Y")
        end_date = datetime.strptime(f"{end_str}/{year}", "%d/%m/%Y")
        date_ranges.append((start_date, end_date))
    return date_ranges


# 定义解析持续时间的函数
def parse_duration(duration_str):
    if "hr" in duration_str:
        hours = int(duration_str.split(" ")[0])
        return hours * 60
    return 0


# 时间标准化为 HHMMSS 格式
def standardize_time(time_str):
    if len(time_str) == 5: 
        time_str = time_str + ":00"
    return time_str


# 创建单个事件的ICS格式字符串
def create_ics_event(code, type_, start, end, location, description, until):
    return (
        "BEGIN:VEVENT\n"
        f"SUMMARY:{code}-{type_}\n"  
        f"DTSTART:{start.strftime('%Y%m%dT%H%M%S')}\n"
        f"DTEND:{end.strftime('%Y%m%dT%H%M%S')}\n"  # 添加DTEND为事件结束时间
        f"RRULE:FREQ=WEEKLY;UNTIL:{until.strftime('%Y%m%dT%H%M%S')}\n"  # UNTIL为整个周期的结束日期
        f"LOCATION:{location}\n"
        f"DESCRIPTION:{description}\n" 
        "END:VEVENT\n"
    )


# 读取CSV并生成ICS内容
def generate_ics_from_csv(csv_file_path, ics_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\n"

        for row in reader:

            event_duration = parse_duration(row["Duration"])

            time_str = standardize_time(row["Time"])
            time_start = datetime.strptime(time_str, "%H:%M:%S")

            weeks_ranges = parse_weeks(row["Weeks"], row["Year"])

            name = row["Name"]
            classroom = row["Classroom"]

            description = (f"Name: {name} | Classroom: {classroom}")

            for start_date, end_date in weeks_ranges:
                # 设置一个标记，确保每个事件只被添加一次
                event_added = False

                current_date = start_date

                while current_date <= end_date:
                    day_mapping = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
                    day_offset = day_mapping[row["Day"]]

                    # 如果当前日期是需要的日期，则生成事件
                    if current_date.weekday() == day_offset and not event_added:
                        event_start = datetime.combine(current_date, time_start.time())
                        event_end = event_start + timedelta(minutes=event_duration)

                        event_until = end_date  

                        # 创建ICS事件并添加到内容中
                        ics_content += create_ics_event(
                            code=row["Code"],
                            type_=row["Type"],  
                            start=event_start,
                            end=event_end,
                            location=row["Location"],
                            description=description,  
                            until=event_until 
                        )
                        event_added = True  
                    current_date += timedelta(days=1)

        ics_content += "END:VCALENDAR\n"

    # 将ICS内容保存到文件
    with open(ics_file_path, 'w', encoding='utf-8') as f:
        f.write(ics_content)


# 输入CSV路径和输出ICS路径
csv_file_path = 'schedule.csv'  
ics_file_path = 'schedule.ics'  

# 调用函数生成ICS文件
generate_ics_from_csv(csv_file_path, ics_file_path)
print(f"ICS文件已生成：{ics_file_path}")
