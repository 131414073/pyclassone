from sys import exit

def start():
    print("话说唐僧师徒四人跋山涉水，终于来到了传说中的白骨山上.")
    print("唐僧：徒儿，这里是个什么去处？真是太~~~~~好看啦！哎？怎么没有人烟？")
    print("悟空：嗯，这里妖气十足，可能会有妖怪吧!我们都要小心哪。那个p猪儿喃？")
    print("八戒:哎呀！我饿了麻。我要吃肉肉 就要吃肉肉.")
    print("悟空：吃吃吃！就晓得吃！老子一指拇儿do死你个gr的")
    print("八戒:师傅!你看猴儿欺负我.555~")
    print("唐僧：空空，你天天按到那个猪儿弄。他长得有好乖迈？")
    print("唐僧：空空，不是我说你，你干点正经的事麻.")
    print("唐僧：像什么《西游十大约会场所》《西游五大最美夜景》《约会手册》。。。之类的，你要多看看！")
    print("唐僧：书中自有黄金屋麻。。")
    print("悟空：.......")
    print("悟空：好好好，说不过你我去找吃的.")
    print("某处山洞中。。")
    print("白骨精:《西游报》头版头条唐僧取经今日将到达白骨岭，哈哈！")
    print("莫非是我期待已久的唐僧来了？吃了他的肉，不但可以延年益寿，长生不老，还可以止咳化痰、清咽润喉...咳咳！")
    print("上天安排的机会，我们没有理由错过的！")
    print("2个小妖：好的大王，是的大王！")
    print("白骨精:恩？说过多少次了，不要叫我大王，要叫我女王大人！")
    print("2个小妖：好的大王，是的大王！")
    print("白骨精:......")
    print("白骨精说：那我抓到唐僧后怎么吃呢")
    print("小妖甲说：烤着吃、炒着吃、炖着吃!")
    print("小妖乙说：我说炸着吃，再蘸上甜辣酱、番茄酱、千岛酱、芥末油、老干妈辣酱。。。。。。")
    print("白骨精说：歌～舞～恩～，滚！")
    print("接着，白骨精念了一段咒语（拉吧吧能量！乌拉乌拉，小魔仙全身变！），将自己变成了一个美女。")
    print("1. 拉吧吧能量！乌拉乌拉，小魔仙全身变！")
    print("2. 古拉拉黑暗之神！呜呼啦呼，黑魔变身！")
    choice = input("> ")
    if choice == "1":
        print("变成了一个美女")
        adventure_room()

    elif choice == "2":
        print("变成了一个丑逼")
        print("是否继续？　是／否.")
        choice = input("> ")
        if choice == "是":
            start()
        elif choice == "否":
            print("再见!")

def adventure_room():
    print("a few time letter..")
    print("八戒：哎！我都前胸贴后背了猴哥还没回来！")
    print("沙僧：是阿。我去那边看看！")
    print("这时一位美女提着篮子款款走上前来，篮子里面放满了好吃的。")
    print("八戒走出去，眼巴巴地看着白骨精的篮子。")
    print("八戒：你篮子里面是啥？")
    print("哦，也没什么，只是些蛋黄派呀、炸鸡腿呀、巧克力呀、水果糖什么的.不过出家人不是不吃荤吗？")
    print("八戒说：我师傅是不吃荤的，你有甜玉米棒吗？我什么都能吃，不挑食，巨无霸呀、炸鸡翅呀、上校鸡块呀我都能吃。最喜欢超级至尊披萨。")
    print("这时悟空回来了..")
    print("1. 啊哒！妖怪看棒！")
    print("2. 没注意白骨精。。")
    choice = input("> ")
    if choice == "1":
        print("悟空当头一棒敲死了白骨精，打得是稀里哗啦，尸骨无存。。")
        adventure_room1()

    elif choice == "2":
        print("唐僧被用技拐走了。。")
        print("唐僧卒，享年38岁。。")
        print("是否继续？　是／否.")
        choice = input("> ")
        if choice == "是":
            start()
        elif choice == "否":
            print("再见!")
    else:
        adventure_room()

def adventure_room1():
    print("唐僧：哎哟我草!这么劲爆的吗?")
    print("唐僧：咳咳咳！不对不对。。。空空！你又滥杀无辜。")
    print("唐僧：这可是一条人命阿！你一下把他打的尸骨无存，这。。。这拿来油炸清蒸吃了多好啊？")
    print("八戒:......")
    print("沙僧:......")
    print("悟空:我在去看看妖怪去哪里了！")
    print("唐僧:......")
    print("旁白：白骨精一计不成，又摇身变了一个老奶奶。")
    print("老太太：女儿啊，女儿，你在哪？")
    print("八戒:你看人家妈妈来找女儿了，还说人家是妖怪。")
    print("老太太：请问你有没有看见我的女儿？")
    print("八戒、沙僧纷纷摇头。老奶奶突然看见了装食物的篮子，猛走过去，提起篮子")
    print("老奶奶：我的女儿呢，你们把我的女儿藏哪里了，你们一定打死了我的女儿!")
    print("老奶奶：我今天，我。。％＊￥＆￥％￥他妈＊＃＾的＃％＾＃＊老子！＄＊！(无限马赛克)")
    print("旁白：突然，白骨精变了回来，把唐僧和八戒拐走了。可怜的沙僧又一次被无视了。")
    print("这时候，孙悟空没有追到白骨精，回来了..他看见。。看见沙僧正靠在一棵树后咬手指甲。")
    print("3师弟，师傅和2师弟呢？")
    print("沙僧：哦，他们上厕所去了。")
    print("悟空：“不对吧，以往我一出现，你说的第一句话就是：大师兄!师傅被妖怪抓走了！")
    print("第二句是：大师兄，二师兄被妖怪抓走了！接着是：大师兄，师傅和二师兄被妖怪抓走了！")
    print("第四句是：大师兄，我们快去救他们吧！")
    print("沙僧：......")
    print("悟空：等等，让我来推理一下！（片刻后）哼哼，真相只有一个！师傅和二师兄被抓到白骨精开的麦当捞里去了！")
    print("沙僧：那我们赶快去吧！")
    print("1. 走路")
    print("2. TAXI")
    print("3. 滴滴打车")
    choice = input("> ")
    if choice == "1":
        print("悟空沙僧安全到达目的地..")
        adventure_room2()
    elif choice == "2":
        print("悟空叫到了一辆车，没想到司机是个妖怪，把悟空沙僧拖到了阴沟里。。")
        print("是否继续？　是／否.")
        choice = input("> ")
        if choice == "是":
            adventure_room1()
        elif choice == "否":
            print("再见!")
    elif choice == "3":
        print("悟空拿出了小米6x，但信号不好。。打了一辆三轮车。。中途爆胎，掉下了悬崖.")
        print("是否继续？　是／否.")
        choice = input("> ")
        if choice == "是":
            adventure_room1()
        elif choice == "否":
            print("再见!")
def adventure_room2():
    print("白骨精：让我想想你们俩怎么吃吧！唐僧嘛，细皮嫩肉的，就做香辣唐僧肉")
    print("白骨精：猪八戒就做成田园猪肉堡，吃不完的就做成八戒薯条，卖给蜘蛛精那的肯德气去！ahhhh")
    print("正当白骨精准备下手时，孙悟空和沙僧赶到.")
    print("悟空：白骨精你个老妖怪！快快放了我师傅和二师弟，我就饶了你！")
    print("白骨精：切，奥巴马来了我都不放！")
    print("悟空：好啊你，敬酒不吃吃罚酒是吧！诶，白骨精，你后面是奥巴马！！")
    print("白骨精：shit！..哎哟奥巴马,马哥，我错了，错了，我不该说你坏话，我不该。。哎？个死猴子!")
    print("敢骗你老娘！找打。")
    print("悟空：不好意思我是石头里面的。。")
    print("白骨精：你!..噗哇！(一口老血)")
    print("悟空：看我的打狗棒！")
    print("1. 打12次")
    print("2. 1次")
    print("3. 9次")
    print("4. 3次")
    print("5. 10次")
    print("6. 5次")
    print("7. 8次")
    choice = input("> ")
    if choice == "1":
        print("你被白骨精反手一耳屎掺死了。。。。")
        print("是否继续？　是／否.")
        choice = input("> ")
        if choice == "是":
            adventure_room2()
        elif choice == "否":
            print("再见!")
    elif choice == "2":
        print("你被白骨精反手一耳屎掺死了。。。。")
        print("是否继续？　是／否.")
        choice = input("> ")
        if choice == "是":
            adventure_room2()
        elif choice == "否":
            print("再见!")
    elif choice == "3":
        print("你被白骨精反手一耳屎掺死了。。。。")
        print("是否继续？　是／否.")
        choice = input("> ")
        if choice == "是":
            adventure_room2()
        elif choice == "否":
            print("再见!")
    elif choice == "4":
        print("白骨精：啊---！")
        print("悟空：（神气而又自负地朝棒子吹一口气）：你个怂逼！")
        print("沙僧（把唐僧和八戒救下来）：师傅，你没事吧？")
        print("唐僧：手好象有些骨折！")
        print("沙僧：那去2医院吧！")
        print("唐僧：不去，这年头看病贵又难，咱伤不起呀！")
        print("悟空（揪住八戒耳朵）：你是头猪啊！连师傅都看不住！")
        print("八戒：我本来就是头猪嘛！")
        print("悟空：我.....")
    elif choice == "5":
        print("你被白骨精反手一耳屎掺死了。。。。")
        print("是否继续？　是／否.")
        choice = input("> ")
        if choice == "是":
            adventure_room2()
        elif choice == "否":
            print("再见!")
    elif choice == "6":
        print("你被白骨精反手一耳屎掺死了。。。。")
        print("是否继续？　是／否.")
        choice = input("> ")
        if choice == "是":
            adventure_room2()
        elif choice == "否":
            print("再见!")
    elif choice == "7":
        print("你被白骨精反手一耳屎掺死了。。。。")
        print("是否继续？　是／否.")
        choice = input("> ")
        if choice == "是":
            adventure_room2()
        elif choice == "否":
            print("再见!")

start()