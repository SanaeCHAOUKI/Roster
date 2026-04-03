# -*- coding: utf-8 -*-
import re
from employees.models import Notification

notifs = Notification.objects.all()
updated = 0

for n in notifs:
    msg = n.message
    original = msg

    # Remplacer emojis par tags
    msg = msg.replace('\U0001f3d6\ufe0f', '[conge]')  # 🏖️
    msg = msg.replace('\U0001f3d6', '[conge]')          # 🏖
    msg = msg.replace('\U0001f4c4', '[doc]')            # 📄
    msg = msg.replace('\u2795', '[add]')                # ➕
    msg = msg.replace('\u270f\ufe0f', '[edit]')         # ✏️
    msg = msg.replace('\u270f', '[edit]')               # ✏
    msg = msg.replace('\U0001f52e', '[pred]')           # 🔮
    msg = msg.replace('\U0001f4b0', '[paie]')           # 💰
    msg = msg.replace('\u2705', '[ok]')                 # ✅
    msg = msg.replace('\u274c', '[ko]')                 # ❌
    msg = msg.replace('\U0001f514', '')                 # 🔔
    msg = re.sub(r'\s+', ' ', msg).strip()

    if msg != original:
        n.message = msg
        n.save(update_fields=['message'])
        updated += 1
        print('OK: ' + msg[:60])

print('Total mis a jour: ' + str(updated) + ' / ' + str(notifs.count()))
