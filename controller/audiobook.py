import util  # 自定义
import dbutil  # 自定义
import re  # 第三方
from lxml import etree  # 第三方
from datetime import date  # python 自带
import time  # 系统自带
import traceback  # 系统自带
import re  # 系统自带


# --------------------------------------------------------------------------- #
# 创建一个线程--》下载书
# Parameter1: category_url 某个类别的首页url
# Parameter2: category_dict 类别对照表, html里的categoryid --> 数据库typeid
# Parameter3: sleep_time(int秒) 每爬一个url 休眠时间
# output: None
# return: json
# --------------------------------------------------------------------------- #
# 创建一个线程--》下载书
def spider_audiobook(category_url, category_dict, sleep_seconds):
    # 思路：
    # 1. 从一个网站的url (各种分类的url,几个分类起几个线程)
    # 2. 爬取所有书的信息
    # 3. 存入数据库

    # 1. 从一个网站的url (各种分类的url,几个分类起几个线程)
    # 玄幻 https://www.tingbook.cc/book/1.html
    # 武侠 https://www.tingbook.cc/book/2.html
    # 都市 https://www.tingbook.cc/book/3.html
    # 言情 https://www.tingbook.cc/book/4.html
    # 科幻 https://www.tingbook.cc/book/5.html
    # 推理 https://www.tingbook.cc/book/6.html
    # 恐怖 https://www.tingbook.cc/book/7.html
    # 惊悚 https://www.tingbook.cc/book/8.html
    # 历史 https://www.tingbook.cc/book/9.html
    # 军事 https://www.tingbook.cc/book/10.html
    # 网游 https://www.tingbook.cc/book/11.html
    # 官商 https://www.tingbook.cc/book/12.html
    # 评书 https://www.tingbook.cc/book/13.html
    # 相声 https://www.tingbook.cc/book/14.html
    # 文学 https://www.tingbook.cc/book/15.html
    # 儿童 https://www.tingbook.cc/book/16.html
    # 穿越 https://www.tingbook.cc/book/28.html
    # 娱乐 https://www.tingbook.cc/book/29.html
    # 笑话 https://www.tingbook.cc/book/30.html
    # 戏曲 https://www.tingbook.cc/book/31.html
    # 其它 https://www.tingbook.cc/book/32.html
    # 百家讲坛 https://www.tingbook.cc/book/33.html
    # 评书专区 https://www.52pingshu.com/
    # app下载 https://tingbook.cc/downapp/

    # 0. 初始化
    default_result = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    try:
        audiobook_url_prefix = dbutil.audiobook_url_prefix

        # 1. 从一个网站的url (各种分类的url,几个分类起几个线程)，只需给出某个分类的第一页数据即可，自动获取尾页号码
        html_str = util.get_html(category_url)  # https://www.tingbook.cc/book/1.html
    #     html_str = """
        # #         <!DOCTYPE html>
        # # <html>
        # #     <head>
        # #         <meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0">
        # #         <meta http-equiv="X-UA-Compatible" content="IE=edge">
        # #         <meta name="renderer" content="webkit">
        # #         <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        # # <title>玄幻有声小说_第1页_听书网有声小说_听书网有声小说</title>
        # # <meta name="keywords"content="在线听书网,免费听书网,玄幻,玄幻有声小说"/>
        # # <meta name="description"content="听书网有声小说为您整理收集最新免费的玄幻有声小说,玄幻有声小说在线听书,免费听书网."/>
        # #         <link href="/templets/tingshu/images/favicon_tx.ico" type="image/x-icon" rel="icon"/>
        # #         <link rel="stylesheet" rev="stylesheet" href="/templets/tingshu/images/iconfont.css" type="text/css" media="all" />
        # #         <link rel="stylesheet" rev="stylesheet" href="/templets/tingshu/images/shiui.min.css" type="text/css" media="all" />
        # #         <link rel="stylesheet" rev="stylesheet" href="/templets/tingshu/images/txcstx.css" type="text/css" media="all" />
        # # <script type="text/javascript" src="/js/common.js"></script>
        # # <script type="text/javascript" src="/js/function.js"></script>
        # # <script type="text/javascript">var sitePath='', siteUrl='http://www.tingbook.cc'</script>
        # #         <style>
        # #             body{background-color: #e9faff;color: #5a5a5a;}
        # #             a{color: #4a4a4a;}
        # #             a:hover,.tx-c1{color: #1e7fa0;}
        # #             .nav,.nav li ul li a:hover,.style-btn:hover,.info-next a:hover,.pagebar a:hover,.pagebar .now-page,.search-page button,.tx-color,.search-post button{background-color:#1e7fa0;}
        # #             .nav>ul>li:hover>a,.nav li.on>a{background-color:#115069;}
        # #             .tx-box2,.tx-title2,.style-btn,.info-li .tx-title2,.info-next a,.search-page form{border-color:#1e7fa0;}
        # #             .top,.tx-box,.tx-title1,.ul-b li,.row-b li,.info-li li,.tx-input,.tx-textarea,.tx-user-box1::before,.user-nav li,.tx-text hr,
        # # .tx-hr,.msg,.place{border-color:#7bcbd9;}
        # #             .user-nav li.on a{background-color:#7bcbd9;}
        # #             .tx-box{background-color:#fef9ef;}
        # #             .tx-box2,.top{background-color:#e2f2f6;}
        # #             @media screen and (max-width: 992px){.info-li li:nth-child(3n){border-color:#7bcbd9;}}
        # #         </style>
        # #         <script src="/templets/tingshu/images/jquery-2.2.4.min.js" type="text/javascript"></script>
        # #         <link rel="stylesheet" type="text/css" href="/templets/tingshu/images/ytuser.css"/>
        # #     </head>
        # #     <body>
        # #                 <div class="top f-12 txt-ov">
        # #             <div class="wide">
        # #                 <span>欢迎来到听书网有声小说</span>
        # #                 <div class="fr">
        # #                     <span class="waphide">听书网有声小说不间断更新最新小说！</span>
        # #                                         <span class="ml15">
        # #                                         <a href="/member.php">会员中心</a>
        # #                                         </span>
        # #                                     </div>
        # #             </div>
        # #         </div>
        # #
        # #         <div class="wide">
        # #             <div class="header clearfix">
        # #                 <div class="logo fl"><a href="/" title="听书网有声小说"><img src="/templets/tingshu/images/logo_tx.png" alt="听书网有声小说"></a></div>
        # #                 <a href="javascript:;" class="nav-on fr pchide"><i class="iconfont icon-unorderedlist f-18"></i></a>
        # #                 <a href="javascript:;" class="search-on fr pchide mr15"><i class="iconfont icon-search icon-close-circle f-18"></i></a>
        # #                                 <div class="search fl waphide">
        # #                     <div class="search-post">
        # # <form  method="get" action="/search.php">
        # #                         <input placeholder="小说作者/名称/播音"  name="searchword">
        # # <button class="submit search_submit" id="searchbutton"><i class="iconfont icon-search"></i></button>
        # # </form>
        # #                     </div>
        # #                 </div>
        # #                             </div>
        # #
        # #                         <div class="nav mb10">
        # #                 <ul class="clearfix">
        # # <li id="nvabar-item-index"><a href="/">首页</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/1.html">玄幻</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/2.html">武侠</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/3.html">都市</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/4.html">言情</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/5.html">科幻</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/6.html">推理</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/7.html">恐怖</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/8.html">惊悚</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/9.html">历史</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/10.html">军事</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/11.html">网游</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/12.html">官商</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/13.html">评书</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/14.html">相声</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/15.html">文学</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/16.html">儿童</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/28.html">穿越</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/29.html">娱乐</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/30.html">笑话</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/31.html">戏曲</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/32.html">其它</a></li>
        # #
        # # <li id="navbar-category-2"><a href="/book/33.html">百家讲坛</a></li>
        # #
        # # <li><a href="https://www.52pingshu.com/">评书专区</a></li>
        # # <li><a href="https://tingbook.cc/downapp/"><h3><span style="color: red;">APP下载</span></h3></a></li>
        # #                 </ul>
        # #             </div>
        # # <div class="tx-box mb10">
        # #     <div class="place f-12">当前位置：<a href='/index.html' >首页</a>&nbsp;&nbsp;&raquo;&nbsp;&nbsp;<a href='/book/1.html' >玄幻</a></div>
        # #     <ul class="row3 row-b">
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/32435.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/211214/2934c0d3b45c57a9.gif" alt="楚王妃"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 雷鬼</span><a href="/show/32435.html" class="f-bold">楚王妃</a></h2>
        # #                                         <p class="f-gray mb10 f-12">楚王妃作者：雷鬼，由宁儿播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/32435.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/25993.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210731/bdb4a8d7dc48809e.gif" alt="绝世武神"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 亦笑天有声工作室</span><a href="/show/25993.html" class="f-bold">绝世武神</a></h2>
        # #                                         <p class="f-gray mb10 f-12">绝世武神作者：亦笑天有声工作室，由净无痕播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/25993.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/25885.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210519/0eb6e727c9b596b2.gif" alt="大奉打更人"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 掌易灵动</span><a href="/show/25885.html" class="f-bold">大奉打更人</a></h2>
        # #                                         <p class="f-gray mb10 f-12">大奉打更人作者：掌易灵动，由卖报小郎君播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/25885.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/25884.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="https://www.lrts5.com/uploads/allimg/210518/7505a129287c57b8.gif#err" alt="吞天"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 本良 一诺</span><a href="/show/25884.html" class="f-bold">吞天</a></h2>
        # #                                         <p class="f-gray mb10 f-12">吞天作者：本良 一诺，由妖白菜播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/25884.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/25683.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210419/e6f00fdf9403b300.gif" alt="异世流放"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 小白 妖仙</span><a href="/show/25683.html" class="f-bold">异世流放</a></h2>
        # #                                         <p class="f-gray mb10 f-12">异世流放作者：小白 妖仙，由易人北播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/25683.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/25666.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="https://img.iyeren.com/ximafm/uploads/allimg/210405/64dbe58b87f04daf.gif#err" alt="我有九个女徒弟"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 同桌 凌烟</span><a href="/show/25666.html" class="f-bold">我有九个女徒弟</a></h2>
        # #                                         <p class="f-gray mb10 f-12">我有九个女徒弟作者：同桌 凌烟，由毕竟是蠢材播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/25666.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/25806.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="https://www.lrts5.com/uploads/allimg/210504/b1e615d8e02bb8b5.gif#err" alt="沧元图"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 华音传媒</span><a href="/show/25806.html" class="f-bold">沧元图</a></h2>
        # #                                         <p class="f-gray mb10 f-12">沧元图作者：华音传媒，由我吃西红柿播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/25806.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/25645.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210316/e6098f64546c8fa3.gif" alt="元龙"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 钟健 周玢</span><a href="/show/25645.html" class="f-bold">元龙</a></h2>
        # #                                         <p class="f-gray mb10 f-12">元龙作者：钟健 周玢，由任怨播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/25645.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/25630.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210301/069e454744191979.gif" alt="万族之劫"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 刺儿 龚玺</span><a href="/show/25630.html" class="f-bold">万族之劫</a></h2>
        # #                                         <p class="f-gray mb10 f-12">万族之劫作者：刺儿 龚玺，由老鹰吃小鸡播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/25630.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/25613.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210220/f0142d2b0a50bc88.gif" alt="我师兄实在太稳健了"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 墨客 伽蛮菌</span><a href="/show/25613.html" class="f-bold">我师兄实在太稳健了</a></h2>
        # #                                         <p class="f-gray mb10 f-12">我师兄实在太稳健了作者：墨客 伽蛮菌，由言归正传播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/25613.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/25088.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/201225/e61b37703c6e71fe.gif" alt="绝世武魂"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 领先声创</span><a href="/show/25088.html" class="f-bold">绝世武魂</a></h2>
        # #                                         <p class="f-gray mb10 f-12">绝世武魂作者：领先声创，由洛城东播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/25088.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/25087.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/201225/462aa1b81c0a6ae0.gif" alt="斗罗大陆4终极斗罗"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 骤雨惊弦</span><a href="/show/25087.html" class="f-bold">斗罗大陆4终极斗罗</a></h2>
        # #                                         <p class="f-gray mb10 f-12">斗罗大陆4终极斗罗作者：骤雨惊弦，由唐家三少播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/25087.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/25138.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/201225/3e7eb470e73ffcc6.gif" alt="九转道经"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 壮则思飞</span><a href="/show/25138.html" class="f-bold">九转道经</a></h2>
        # #                                         <p class="f-gray mb10 f-12">九转道经作者：壮则思飞，由天茗播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/25138.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/25128.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/201225/aebb8251df902742.gif" alt="九星霸体诀"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 舟扬</span><a href="/show/25128.html" class="f-bold">九星霸体诀</a></h2>
        # #                                         <p class="f-gray mb10 f-12">九星霸体诀作者：舟扬，由平凡魔术师播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/25128.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/25958.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210629/1a5a6d9b6b87e5d9.gif" alt="神魔天尊"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 丹羽道 浥轻尘 曉夢</span><a href="/show/25958.html" class="f-bold">神魔天尊</a></h2>
        # #                                         <p class="f-gray mb10 f-12">神魔天尊作者：丹羽道 浥轻尘 曉夢，由九当家播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/25958.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #                         <li class="col-12 col-m-24 col3-">
        # #             <div class="style-img clearfix">
        # #                 <a href="/show/25634.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210308/99fc1fa1506d6510.gif" alt="神魂丹帝"></span></a>
        # #                 <section>
        # #                     <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 果维听书</span><a href="/show/25634.html" class="f-bold">神魂丹帝</a></h2>
        # #                                         <p class="f-gray mb10 f-12">神魂丹帝作者：果维听书，由浊酒一湖播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
        # #                     <p><a href="/show/25634.html" class="style-btn tx-c1">开始收听</a></p>
        # #                 </section>
        # #             </div>
        # #         </li>
        # #
        # #             </ul>
        # # </div>
        # #
        # # <div class="pagebar ta-c mb15"><span>
        # #             <a href="/book/1.html"><span class="page">首页</span></a>
        # #             <a href="/book/1-0.html" ><span class="page">‹‹</span></a>
        # #
        # #                 <span class="page now-page">1</span>
        # #
        # #                 <a href="/book/1-2.html" ><span class="page">2</span></a>
        # #
        # #                 <a href="/book/1-2.html" ><span class="page">››</span></a>
        # #             <a href="/book/1-113.html"><span class="page">尾页</span></a>
        # #             </span>
        # # </div>
        # #
        # #
        # #
        # #
        # # <div class="footer ta-c f-12">
        # # 	<a href="" target="_blank" title="关于我们">关于我们</a> - <a href="/gbook.php" target="_blank" title="投诉举报">投诉举报</a> - <a href="/gbook.php" target="_blank" title="留言反馈">留言反馈</a> - <a href="/xml/baidu.xml" target="_blank" title="网站地图">网站地图</a><br><br>免责声明：本站资源来源于网络，版权归原作者所有，若有侵犯您的权利，请来信告知，我们将立即予以删除。！<br>
        # #     <p>Powered By <a href="/" title="听书网" target="_blank">听书网--邮箱：5261287@qq.com</a>
        # # <script>
        # # var _hmt = _hmt || [];
        # # (function() {
        # #   var hm = document.createElement("script");
        # #   hm.src = "https://hm.baidu.com/hm.js?2b17643065761366d8a45ded7a8f69cf";
        # #   var s = document.getElementsByTagName("script")[0];
        # #   s.parentNode.insertBefore(hm, s);
        # # })();
        # # </script>
        # #  </p>
        # #     Copyright Your WebSite.Some Rights Reserved.</div>
        # # </div>
        # # <div class="nav-off"></div>
        # # <div class="gotop tx-color"><i class="iconfont icon-caret-up"></i></div>
        # #
        # # <div class="side-gg gg-box side1"><a href="#"><img src="/templets/tingshu/images/gg2.jpg"></a><a href="javascript:;" class="gg-off"><i class="iconfont icon-close-circle"></i></a></div>
        # # <div class="side-gg gg-box side2"><a href="#"><img src="/templets/tingshu/images/gg2.jpg"></a><a href="javascript:;" class="gg-off"><i class="iconfont icon-close-circle"></i></a></div>
        # # <script src="/templets/tingshu/images/txcstx.js"></script>
        # #
        # # </body>
        # # </html>
        # #     """

        endpage_url = util.get_list_from_str_by_regexp(r'a\shref="(.*)"><span\sclass="page">尾页', html_str)[0]
        print('尾页号码= ', endpage_url)
        # /book/1-113.html
        categoryid = int(util.get_list_from_str_by_regexp(r'/(\d+)-', endpage_url)[0])  # 网站某个分类，html 里的 数字代表值, /后 -前的数字,
        endpagenum = int(util.get_list_from_str_by_regexp(r'-(\d+)\.', endpage_url)[0])  # 尾页名称， -后 .前的数字

        # 2. 循环爬取某分类下所有书
        for index in range(endpagenum):
            try:
                # 前缀/book/categoryid-index.html  index从0开始
                spider_url = audiobook_url_prefix + '/book/' + str(categoryid) + '-' + str(index+1) + '.html'  # 爬取url
                print('爬取网页url = ', spider_url)
                html_str = util.get_html(spider_url)

                # lxml 爬取当前页 书名、封面图片、演播作者、简介、书的url(不带前缀插入数据库-》网站的前缀写在配置文件中)
                dom = etree.HTML(html_str)
                booknames = dom.xpath('//div[@class="style-img clearfix"]//section/h2/a[@class="f-bold"]/text()')
                print('书名len=%s, list=%s ' % (len(booknames), booknames))
                readers = dom.xpath('//div[@class="style-img clearfix"]//section/h2/span/text()')
                print('播音len=%s, list=%s ' % (len(readers), readers))
                briefs = dom.xpath('//div[@class="style-img clearfix"]//section/p[@class="f-gray mb10 f-12"]/text()')
                print('简介len=%s, list=%s ' % (len(briefs), briefs))
                # covers = dom.xpath('//div[@class="style-img clearfix"]/a[@class="img-80 fl mr1"]/img/@src')
                covers = dom.xpath('//div[@class="style-img clearfix"]/a/span/img/@src')
                print('封面img len=%s, list=%s ' % (len(covers), covers))
                bookurls = dom.xpath('//div[@class="style-img clearfix"]/section/p/a/@href')
                print('书url len=%s, list=%s ' % (len(bookurls), bookurls))
                traditional_booknames = booknames
                simple_booknames = []

                # 数据清洗，书名--》简体
                if len(booknames) > 0:
                    for index, bookname in enumerate(booknames):
                        simple_booknames.append(util.traditional2simple(bookname))  # 转成简体
                        traditional_booknames[index] = util.simple2traditional(booknames[index])  # 转成繁体
                print('简体书名len=%s, list=%s ' % (len(simple_booknames), simple_booknames))
                print('繁体书名len=%s, list=%s ' % (len(traditional_booknames), traditional_booknames))

                # 循环插入数据库
                for i in range(len(simple_booknames)):
                    try:
                        # sql 默认参数
                        sqlvaluedict_default = dict()
                        sqlvaluedict_default.update({
                            "name": "",
                            "traditional_name": "",
                            "url": "",
                            "typeid": category_dict[str(categoryid)],
                            "type": category_dict['type' + str(categoryid)],
                            "countryid": 1,
                            "country": "其它",
                            "processid": 1,
                            "process": "其它",
                            "websiteid": 2,
                            "website": "听书网",
                            "alias": "",
                            "author": "",
                            "reader": "",
                            "brief": "",  # 简介
                            "is_for_adult": "",
                            "score": "",
                            "total_chapter": 0,
                            "cover_photo_url": "",
                            "cover_photo_savepath": "",
                            "hits": 0,  # 点击率
                            "release_date": date.today().strftime('%Y-%m-%d'),  # 当天
                            "last_update_date": date.today().strftime('%Y-%m-%d'),  # 最后更新时间--》当天
                            "update_to_chapter": 0,  # 更新到第几章
                            "spider_status": 0,  # 爬取状态，爬取,如果能插入到数据库，那就是爬取成功
                            "download_status": 0  # 爬取状态，爬取,如果能插入到数据库，那就是爬取成功
                        })

                        sqlvaluedict_default['name'] = simple_booknames[i]
                        sqlvaluedict_default['traditional_name'] = traditional_booknames[i]
                        sqlvaluedict_default['reader'] = readers[i]
                        sqlvaluedict_default['brief'] = briefs[i]
                        sqlvaluedict_default['cover_photo_url'] = covers[i]
                        sqlvaluedict_default['url'] = "https://www.tingbook.cc" + "/" + bookurls[i]
                        # sql = """
                        #     insert into audiobook(`name`, traditional_name, url, typeid, `type`, countryid, country, processid,
                        #     process, websiteid, website, alias, author, reader, brief, is_for_adult,
                        #     score, total_chapter, cover_photo_url, cover_photo_savepath, hits,
                        #     release_date, last_update_date, update_to_chapter, spider_status, download_status)
                        #     values( %(name)s, %(traditional_name)s, %(url)s, %(typeid)s, %(type)s, %(countryid)s, %(country)s, %(processid)s,
                        #     %(process)s, %(websiteid)s, %(website)s, %(alias)s, %(author)s, %(reader)s, %(brief)s, %(is_for_adult)s,
                        #     %(score)s, %(total_chapter)s, %(cover_photo_url)s, %(cover_photo_savepath)s, %(hits)s,
                        #     %(release_date)s, %(last_update_date)s, %(update_to_chapter)s, %(spider_status)s, %(download_status)s)
                        #     on duplicate key update
                        #     `name`=%(name)s, traditional_name=%(traditional_name)s, url=%(url)s, typeid=%(typeid)s, `type`=%(type)s,
                        #     countryid=%(country)s, country=%(country)s, processid=%(processid)s, process=%(process)s,
                        #     websiteid=%(websiteid)s, website=%(website)s, alias=%(alias)s, author=%(author)s, reader=%(reader)s,
                        #     brief=%(brief)s, is_for_adult=%(is_for_adult)s, score=%(score)s, total_chapter=%(total_chapter)s,
                        #     cover_photo_url=%(cover_photo_url)s, cover_photo_savepath=%(cover_photo_savepath)s, hits=%(hits)s,
                        #     release_date=%(release_date)s, last_update_date=%(last_update_date)s, update_to_chapter=%(update_to_chapter)s,
                        #     spider_status=%(spider_status)s, download_status=%(download_status)s
                        # """

                        # sql = """
                        #         insert into audiobook(name, traditional_name, url, typeid, `type`, countryid, country, processid,
                        #         process, websiteid, website, alias, author, reader, brief, is_for_adult,
                        #         score, total_chapter, cover_photo_url, cover_photo_savepath, hits,
                        #         release_date, last_update_date, update_to_chapter, spider_status, download_status)
                        #         values( %(name)s, %(traditional_name)s, %(url)s, %(typeid)s, %(type)s, %(countryid)s, %(country)s, %(processid)s,
                        #         %(process)s, %(websiteid)s, %(website)s, %(alias)s, %(author)s, %(reader)s, %(brief)s, %(is_for_adult)s,
                        #         %(score)s, %(total_chapter)s, %(cover_photo_url)s, %(cover_photo_savepath)s, %(hits)s,
                        #         %(release_date)s, %(last_update_date)s, %(update_to_chapter)s, %(spider_status)s, %(download_status)s)
                        #     """

                        # 拼接sql 插入列
                        cols = "("
                        values = "("
                        updates = ""
                        for key, value in sqlvaluedict_default.items():
                            # print("key=%s, value=%s" % (key, value))
                            if value is None or value == "":  # 空
                                # print(key, '===========================================空')
                                pass
                            else:  # 非空
                                # if key == 'name':
                                #     cols += '`name`' + ','  # 拼接插入列
                                # elif key == 'type':
                                #     cols += '`type`' + ','  # 拼接插入列
                                # else:  # --> pymysql 遇到mysql 关键词，不用写成``的形式
                                cols += key + ','  # 拼接插入列
                                values += '%(' + key + ')s,'  # 拼接插入列的value
                                updates += key + '=%(' + key + ')s,'  # 拼接 update 的value
                        cols = cols.strip(",")
                        values = values.strip(",")
                        updates = updates.strip(",")
                        cols += ')'
                        values += ')'
                        print('sql-->cols==', cols)
                        print('sql-->values==', values)

                        # 3. 执行sql
                        addsql = 'insert into audiobook' + cols + ' values' + values + ' on duplicate key update ' + updates
                        dbutil.execute_project('audiobook', addsql, sqlvaluedict_default)
                    except Exception as ex:
                        print('插入book出现异常error: ', ex)
                    continue

                print('爬取完成-》 休眠', sleep_seconds, spider_url)

            except Exception as ex:
                print('爬取网页出现异常error: ', ex)
            time.sleep(sleep_seconds)  # 休眠
            continue  # 有了异常，继续运行

        # 4 返回值
        default_result['code'] = 200
        default_result['msg'] = 'success'
        default_result['count'] = endpagenum
        default_result['date'] = []
    except Exception as ex:
        print('dbutil -->spider_audiobook() 出现异常,执行continue:', ex)
        traceback.print_exc()  # 打印详细报错


    # 这里执行什么，能让报错后，继续运行？
    return default_result


# --------------------------------------------------------------------------- #
# 创建一个线程--》下载章节url,就爬一本书
# Parameter1: website_domain_name  网站域名
# Parameter2: audiobookid 书的id
# Parameter3: audiobookname 书的简体名字
# Parameter4: url 书的链接
# output: None
# return: None
# --------------------------------------------------------------------------- #
# 创建一个线程--》下载章节url
def spider_chapters(website_domain_name, arg_audiobookid, arg_audiobookname, audiobook_url):
    # 思路：
    # 1. 请求书的 url
    # 2. 爬取章节信息
    # 3. 数据清洗
    # 4. 存入章节数据库
    # 5. 修改book 章节总数

    try:
        # 1. 请求书的url
        html_str = util.get_html(audiobook_url)

        # print('解析html')
        cursor = etree.HTML(html_str)
        titles_simple = cursor.xpath('//div[@id="yuedu"]//li/a/@title')  # 章节名称 - 简体
        total = len(titles_simple)
        urls = cursor.xpath('//div[@id="yuedu"]//li/a/@href')  # 章节链接,没有网站地址,只有相对路径 href="/jpplay/32435-0-0.html"
        print(f'爬取 <<{arg_audiobookname}>>  到的所有 titles_simple = {titles_simple}')
        print(f'章节 <<{arg_audiobookname}>> 总数 = {total}')
        print(f'爬取 <<{arg_audiobookname}>> 到的所有urls = {urls}')

        # 3. 数据清洗
        # 4. 存入数据库
        for i in range(total):
            # print(f'插入数据库 {i}')
            # 4. 插入数据库
            values_dict = {
                "chapter_num": str(i+1),
                "name": titles_simple[i],
                "traditional_name": util.simple2traditional(titles_simple[i]),
                "url": website_domain_name + urls[i],
                "audiobookid": arg_audiobookid,
                "audiobookname": arg_audiobookname,
                "release_date": '',
                "last_update_date": '',
                "spider_status": str(0),
                "download_status": str(0)
            }

            sql = """
                    insert into `chapter` (chapter_num, `name`, traditional_name, `url`, audiobookid, audiobookname, 
                    release_date, last_update_date, spider_status, download_status) 
                    values (%(chapter_num)s, %(name)s, %(traditional_name)s, %(url)s, %(audiobookid)s, %(audiobookname)s,
                    %(release_date)s, %(last_update_date)s, %(spider_status)s, %(download_status)s)
                    on duplicate key update 
                    chapter_num=%(chapter_num)s, `name`=%(name)s, traditional_name=%(traditional_name)s, `url`=%(url)s,
                    audiobookid=%(audiobookid)s, audiobookname=%(audiobookname)s, release_date=%(release_date)s,
                    last_update_date=%(last_update_date)s, spider_status=%(spider_status)s, download_status=%(download_status)s
            """
            try:
                dbutil.execute_project('audiobook', sql, values=values_dict)
            except Exception:
                print('audiobook.py for循环,出现异常,func=spider_chapters')
                traceback.print_exc()  # 打印详细报错
            continue

        # 判断插入数据库的 章节数是否
        chapter_insert_num_sql = f"select count(id) from chapter where audiobookid={arg_audiobookid}"
        chapter_inserted_num = dbutil.execute_project('audiobook', chapter_insert_num_sql)[0][0]
        print(f'=======================chapter_insert_num {chapter_inserted_num}')
        update_audiobook_spider_status = 2  # 修改audiobook的 状态,1 完成 2 没爬完
        if total == chapter_inserted_num:
            print('修改audiobook状态为 1111111111111111111111111111111')
            update_audiobook_spider_status = 1
        # 5. 修改book 章节总数
        sql = f"update audiobook set total_chapter=%(total)s, spider_status={update_audiobook_spider_status} where id=%(arg_audiobookid)s"
        values_dict = {
            "total": str(total),
            "arg_audiobookid": str(arg_audiobookid)
        }
        print(f'--------> {arg_audiobookname} 修改audiobook 的章节总数')
        dbutil.execute_project('audiobook', sql, values_dict)

    except Exception as ex:
        print('audiobook.py 出现异常,func=spider_chapters, 直接修改chapter.spider_status=3')
        traceback.print_exc()  # 打印详细报错
        sql = "update audiobook set total_chapter=%(total)s, spider_status=3 where id=%(arg_audiobookid)s"
        values_dict = {
            "total": str(total),
            "arg_audiobookid": str(arg_audiobookid)
        }
        dbutil.execute_project('audiobook', sql, values_dict)


# --------------------------------------------------------------------------- #
# 创建一个线程--》下载章节的 media
# Parameter1: chapter 书的id  arg_chapterid
# Parameter2: chapter-name 书的简体名字 arg_chaptername
# Parameter3: url 章节 的链接 arg_chapterurl
# output: None
# return: None
# --------------------------------------------------------------------------- #
# 创建一个线程--》下载章节的 media
def spider_chapters_medias(arg_chapterid, arg_chaptername, arg_chapterurl):
    # 思路：
    # 1. 请求书的 url
    # 2. 爬取章节-media信息
    # 3. 数据清洗
    # 4. 修改章节数据库

    try:
        # 1. 请求书的url
        html_str = util.get_html(arg_chapterurl)

        media_url = re.findall(r'var\s now="(.+?)";', html_str, re.VERBOSE | re.DOTALL)[0]
        print(f'爬取 <<{arg_chaptername}>>  到的media_url = {media_url}')

        # 3. 数据清洗
        # 4. 修改数据库
        values_dict = {
            "media_url": media_url,
            "spider_status": str(1),
            "id": str(arg_chapterid),
            "name": arg_chaptername,
            "url": arg_chapterurl
        }

        sql = """
                update chapter set media_url=%(media_url)s, spider_status=%(spider_status)s 
                where
                id=%(id)s and name=%(name)s and url=%(url)s
        """
        dbutil.execute_project('audiobook', sql, values=values_dict)

        # 判断插入的media_url是否有值,如果没有,改spider_status=2 (爬取,未成功)
        sql = f"select media_url from chapter where id={arg_chapterid}"
        media_url = dbutil.execute_project('audiobook', sql)[0][0]
        if media_url is None or media_url == "":
            sql = f"update chapter set spider_status=2 where id={arg_chapterid}"
            dbutil.execute_project('audiobook', sql)

    except Exception as ex:
        print('audiobook.py 出现异常,func=spider_chapters_medias, 直接修改chapter.spider_status=3')
        traceback.print_exc()  # 打印详细报错
        sql = "update chapter set spider_status=3 where id=%(id)s and name=%(name)s and url=%(url)s"
        values_dict = {
            "id": str(arg_chapterid),
            "name": arg_chaptername,
            "url": arg_chapterurl
        }
        dbutil.execute_project('audiobook', sql, values_dict)
