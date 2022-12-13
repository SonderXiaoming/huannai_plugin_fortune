def group_rule_str2list(rulestr : str) -> list[str]:
    # 将json中的字符串配置转换成list
    if rulestr[-1] == ',':
        rulestr = rulestr[:-1]
    return(rulestr.split(","))

def group_rule_list2str(group_rule_list : list[str]) -> str:
    gs = ""
    for gr in group_rule_list:
        gs = gs + gr + ","
    gs = gs[:-1]
    return(gs)