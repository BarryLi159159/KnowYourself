from lunar_python import Solar, Lunar

# Define Five Elements and their relationships
five_elements = {
    "金": {"生": "水", "克": "木"},
    "木": {"生": "火", "克": "土"},
    "水": {"生": "木", "克": "火"},
    "火": {"生": "土", "克": "金"},
    "土": {"生": "金", "克": "水"},
}

# Heavenly Stems and their Five Elements
heavenly_stems_elements = {
    "甲": "木", "乙": "木",
    "丙": "火", "丁": "火",
    "戊": "土", "己": "土",
    "庚": "金", "辛": "金",
    "壬": "水", "癸": "水",
}

# Earthly Branches and their Five Elements
earthly_branches_elements = {
    "子": "水", "丑": "土", "寅": "木", "卯": "木", 
    "辰": "土", "巳": "火", "午": "火", "未": "土",
    "申": "金", "酉": "金", "戌": "土", "亥": "水",
}

# Define the Heavenly Stems and Earthly Branches
heavenly_stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
earthly_branches = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

# Step 1: Ask for user's name, gender, and Gregorian date/time of birth
name = input("请输入姓名: ")
year = int(input("请输入公历出生年份 (如: 2023): "))
month = int(input("请输入公历出生月份 (如: 12): "))
day = int(input("请输入公历出生日期 (如: 25): "))
hour = int(input("请输入出生时间 (24小时制, 如: 14): "))

# Step 2: Convert Gregorian date to Lunar date
solar = Solar.fromYmdHms(year, month, day, hour, 0, 0)
lunar = solar.getLunar()

print("\n======== 农历转换结果 ========")
print(f"公历 {year}年{month}月{day}日 转为 农历:")
print(f"{lunar.getYear()}年{lunar.getMonth()}月{lunar.getDay()}日")
print(f"生肖: {lunar.getYearZhi()} ({lunar.getYearShengXiao()})")

# Step 3: Calculate Heavenly Stems and Earthly Branches (天干地支)
eight_char = lunar.getEightChar()
year_gan, year_zhi = eight_char.getYearGan(), eight_char.getYearZhi()
month_gan, month_zhi = eight_char.getMonthGan(), eight_char.getMonthZhi()
day_gan, day_zhi = eight_char.getDayGan(), eight_char.getDayZhi()
time_gan, time_zhi = eight_char.getTimeGan(), eight_char.getTimeZhi()

# Align 天干 and 地支
print("\n======== 天干地支计算结果 ========")
print("天干: ", f"{year_gan}   {month_gan}   {day_gan}   {time_gan}")
print("地支: ", f"{year_zhi}   {month_zhi}   {day_zhi}   {time_zhi}")
print("=================================")

# Create lists for 天干 and 地支
heavenly_stems = [year_gan, month_gan, day_gan, time_gan]
earthly_branches = [year_zhi, month_zhi, day_zhi, time_zhi]

Main_stems = heavenly_stems[2]
Main_elements = heavenly_stems_elements[Main_stems]
print(f"主运: {Main_stems} ({heavenly_stems_elements[Main_stems]})")


#天干五行属性
heavenly_stems_elements = [heavenly_stems_elements[heavenly_stems[0]],heavenly_stems_elements[heavenly_stems[1]],heavenly_stems_elements[heavenly_stems[2]],heavenly_stems_elements[heavenly_stems[3]]]
print(f"天干五行属性: {heavenly_stems_elements}")
#地支五行属性
earthly_branches_elements = [earthly_branches_elements[earthly_branches[0]],earthly_branches_elements[earthly_branches[1]],earthly_branches_elements[earthly_branches[2]],earthly_branches_elements[earthly_branches[3]]]
print(f"地支五行属性: {earthly_branches_elements}")

# Initialize scores
score = 0
score2 = 0

# Evaluate Heavenly Stems (天干) scores
if Main_elements == "金":
    print("主运金，五行属性为金，所以主运金")
    for i in [0, 1, 3]:  # Check the positions to adjust
        if heavenly_stems_elements[i] in ["土", "金"]:  # Corrected conditional
            score += 10

if Main_elements == "木":
    print("主运木，五行属性为木，所以主运木")
    for i in [0, 1, 3]:
        if heavenly_stems_elements[i] in ["水", "木"]:  # Corrected conditional
            score += 10

if Main_elements == "水":
    print("主运水，五行属性为水，所以主运水")
    for i in [0, 1, 3]:
        if heavenly_stems_elements[i] in ["金", "水"]:
            score += 10

if Main_elements == "火":
    print("主运火，五行属性为火，所以主运火")
    for i in [0, 1, 3]:
        if heavenly_stems_elements[i] in ["木", "火"]:
            score += 10

if Main_elements == "土":
    print("主运土，五行属性为土，所以主运土")
    for i in [0, 1, 3]:
        if heavenly_stems_elements[i] in ["火", "土"]:
            score += 10

# # Display Heavenly Stems Score
# print("\n======== 天干得分 ========")
# print(f"天干得分: {score}")

# Evaluate Earthly Branches (地支) scores
if Main_elements == "金":
    #print("主运金，五行属性为金，所以主运金")
    for i in [0, 2, 3]:
        if earthly_branches_elements[i] in ["土", "金"]:
            score2 += 10
    if earthly_branches_elements[1] in ["土", "金"]:  # Special index 1 (40 points)
        score2 += 40

if Main_elements == "木":
    #print("主运木，五行属性为木，所以主运木")
    for i in [0, 2, 3]:
        if earthly_branches_elements[i] in ["水", "木"]:
            score2 += 10
    if earthly_branches_elements[1] in ["水", "木"]:
        score2 += 40

if Main_elements == "水":
    #print("主运水，五行属性为水，所以主运水")
    for i in [0, 2, 3]:
        if earthly_branches_elements[i] in ["金", "水"]:
            score2 += 10
    if earthly_branches_elements[1] in ["金", "水"]:
        score2 += 40

if Main_elements == "火":
    #print("主运火，五行属性为火，所以主运火")
    for i in [0, 2, 3]:
        if earthly_branches_elements[i] in ["木", "火"]:
            score2 += 10
    if earthly_branches_elements[1] in ["木", "火"]:
        score2 += 40

if Main_elements == "土":
    #print("主运土，五行属性为土，所以主运土")
    for i in [0, 2, 3]:
        if earthly_branches_elements[i] in ["火", "土"]:
            score2 += 10
    if earthly_branches_elements[1] in ["火", "土"]:
        score2 += 40

# # Display Earthly Branches Score
# print("\n======== 地支得分 ========")
# print(f"地支得分: {score2}")

# Calculate the final score
final_score = score + score2
print("\n======== 最终得分 ========")   
print(f"最终得分: {final_score}")


# Determine 喜用神 based on 身强 or 身弱
if final_score >= 49:
    print("身强")
    strength = "身强"
    # For 身强: 克主运 or 主运生的五行 is 喜神
    if Main_elements == "金":
        喜神 = "火" "水" # 火克金, 金生水
    elif Main_elements == "木":
        喜神 = "金" "火" # 金克木, 木生火
    elif Main_elements == "水":
        喜神 = "土" "木" #土克水, 水生木
    elif Main_elements == "火":
        喜神 = "水" "土" # 水克火, 火生土
    elif Main_elements == "土":
        喜神 = "木" "金" # 木克土, 土生金
else:
    print("身弱")
    strength = "身弱"
    # For 身弱: 主运 or 生主运的五行 is 喜神
    if Main_elements == "金":
        喜神 = "土" "金" # 土生金
    elif Main_elements == "木":
        喜神 = "水" "木"  # 水生木
    elif Main_elements == "水":
        喜神 = "金" "水" # 金生水
    elif Main_elements == "火":
        喜神 = "木" "火" # 木生火
    elif Main_elements == "土":
        喜神 = "火" "土" # 火生土

# Display 喜神
print("\n======== 喜用神判断 ========")
print(f"主运: {Main_elements}")
print(f"身强/身弱: {strength}")
print(f"喜神: {喜神}")


