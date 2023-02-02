def score_calculation(List):
    rules = {
        "石头":1,
        "剪刀":2,
        "布":3}
    calculation_win = 0
    calculation_draw = 0
    Zhang_Fei = 0
    Guan_Yu = 0
    for i in List:
        if i[0] == "石头":
            rules["剪刀"] = 0
            rules["石头"] = 1
            rules["布"] = 2
        elif i[0] == "剪刀":
            rules["剪刀"] = 1
            rules["石头"] = 2
            rules["布"] = 0
        elif i[0] == "布":
            rules["剪刀"] = 2
            rules["石头"] = 0
            rules["布"] = 1
        Zhang_Fei = rules[i[0]] 
        Guan_Yu = rules[i[1]]
        if Zhang_Fei == Guan_Yu:
            calculation_draw +=1
        elif Zhang_Fei>Guan_Yu:
            calculation_win +=1
    if calculation_draw:
        pos_of_draw = f"平手{calculation_draw}局,"
    else:
            pos_of_draw= ""
    if calculation_win>len(List)-calculation_draw - calculation_win:
        final = f"关羽{len(List)}局赢了{calculation_win}局，{pos_of_draw}关羽胜出"
    elif calculation_win + len(List)-calculation_win-calculation_draw == calculation_draw or len(List) == calculation_draw:
        return "双方打平"
    else:
        final = f"张飞{len(List)}局赢了{len(List)-calculation_draw - calculation_win}局，{pos_of_draw}张飞胜出"
    return final
print(score_calculation([ ["石头", "石头"],["石头", "石头"]]    ) )


