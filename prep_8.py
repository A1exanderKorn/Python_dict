import re


def main(s):
    # match = re.search(r'(new ?@"\.{0,}\" ?-> ?`\.{0,}\ ?).', s)
    # match = re.search(r'(new @"\.{0,}\"', s)
    s = s.replace('\n', ' ')
    s = s.replace('(', '\n')
    s = s.replace(').', '\n')
    ans = {}
    a = re.findall(r'new @\"(.+)\" ?->', s)
    b = re.findall(r'-> ?\`(.+)\ ?\n', s)
    for i in range(len(a)):
        if(b[i][len(b[i]) -1 ] == ' '):
            b[i] = b[i][0:len(b[i]) - 1]
        ans[b[i]] = a[i]
    print(ans)
main('[[ ( new @"tegeer"-> `edisre ). ( new @"edbi_182"-> `riaiser). ( new\n@"tequbi_629" -> `cegeti_736 ). ]]')