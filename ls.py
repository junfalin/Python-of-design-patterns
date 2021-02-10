import os
dirs = [i for i in os.listdir('.') if os.path.isdir(i) and i.endswith("type")]

with open('README.md','w',encoding='utf-8') as fs:
    for d in dirs:
        for file in os.listdir(d):
            with open(os.path.join(d,file),'r',encoding='utf-8') as f:
                text = f.read().splitlines()
                title = text.pop(0)
                raw = '\n'.join(text)
                fs.write(f"""###{title}
```
{raw}
```
---
""")