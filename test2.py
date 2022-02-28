from lxml import html, etree  # 第三方
import requests  # 第三方
import re  # python 自带
from datetime import datetime, date  # python 自带
from zhconv import convert


def traditional2simple(traditional_str):
    simple_str = convert(traditional_str, 'zh-hans')
    return simple_str


def simple2traditional(simple_str):
    traditional_str = convert(simple_str, 'zh-hant')
    return traditional_str


html_str = """
    <!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="renderer" content="webkit">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>玄幻有声小说_第1页_听书网有声小说_听书网有声小说</title>
<meta name="keywords"content="在线听书网,免费听书网,玄幻,玄幻有声小说"/>
<meta name="description"content="听书网有声小说为您整理收集最新免费的玄幻有声小说,玄幻有声小说在线听书,免费听书网."/>
    <link href="/templets/tingshu/images/favicon_tx.ico" type="image/x-icon" rel="icon"/>
    <link rel="stylesheet" rev="stylesheet" href="/templets/tingshu/images/iconfont.css" type="text/css" media="all" />
    <link rel="stylesheet" rev="stylesheet" href="/templets/tingshu/images/shiui.min.css" type="text/css" media="all" />
    <link rel="stylesheet" rev="stylesheet" href="/templets/tingshu/images/txcstx.css" type="text/css" media="all" />
<script type="text/javascript" src="/js/common.js"></script>
<script type="text/javascript" src="/js/function.js"></script>
<script type="text/javascript">var sitePath='', siteUrl='http://www.tingbook.cc'</script>
    <style>
        body{background-color: #e9faff;color: #5a5a5a;}
        a{color: #4a4a4a;}
        a:hover,.tx-c1{color: #1e7fa0;}
        .nav,.nav li ul li a:hover,.style-btn:hover,.info-next a:hover,.pagebar a:hover,.pagebar .now-page,.search-page button,.tx-color,.search-post button{background-color:#1e7fa0;}
        .nav>ul>li:hover>a,.nav li.on>a{background-color:#115069;}
        .tx-box2,.tx-title2,.style-btn,.info-li .tx-title2,.info-next a,.search-page form{border-color:#1e7fa0;}
        .top,.tx-box,.tx-title1,.ul-b li,.row-b li,.info-li li,.tx-input,.tx-textarea,.tx-user-box1::before,.user-nav li,.tx-text hr,
.tx-hr,.msg,.place{border-color:#7bcbd9;}
        .user-nav li.on a{background-color:#7bcbd9;}
        .tx-box{background-color:#fef9ef;}
        .tx-box2,.top{background-color:#e2f2f6;}
        @media screen and (max-width: 992px){.info-li li:nth-child(3n){border-color:#7bcbd9;}}
    </style>
    <script src="/templets/tingshu/images/jquery-2.2.4.min.js" type="text/javascript"></script>
    <link rel="stylesheet" type="text/css" href="/templets/tingshu/images/ytuser.css"/>
</head>
<body>
            <div class="top f-12 txt-ov">
        <div class="wide">
            <span>欢迎来到听书网有声小说</span>
            <div class="fr">
                <span class="waphide">听书网有声小说不间断更新最新小说！</span>
                                    <span class="ml15">
                                    <a href="/member.php">会员中心</a>
                                    </span>
                                </div>
        </div>
    </div>

    <div class="wide">
        <div class="header clearfix">
            <div class="logo fl"><a href="/" title="听书网有声小说"><img src="/templets/tingshu/images/logo_tx.png" alt="听书网有声小说"></a></div>
            <a href="javascript:;" class="nav-on fr pchide"><i class="iconfont icon-unorderedlist f-18"></i></a>
            <a href="javascript:;" class="search-on fr pchide mr15"><i class="iconfont icon-search icon-close-circle f-18"></i></a>
                            <div class="search fl waphide">
                <div class="search-post">
<form  method="get" action="/search.php">
                    <input placeholder="小说作者/名称/播音"  name="searchword">
<button class="submit search_submit" id="searchbutton"><i class="iconfont icon-search"></i></button>
</form>
                </div>
            </div>
                        </div>

                    <div class="nav mb10">
            <ul class="clearfix">
<li id="nvabar-item-index"><a href="/">首页</a></li>

<li id="navbar-category-2"><a href="/book/1.html">玄幻</a></li>

<li id="navbar-category-2"><a href="/book/2.html">武侠</a></li>

<li id="navbar-category-2"><a href="/book/3.html">都市</a></li>

<li id="navbar-category-2"><a href="/book/4.html">言情</a></li>

<li id="navbar-category-2"><a href="/book/5.html">科幻</a></li>

<li id="navbar-category-2"><a href="/book/6.html">推理</a></li>

<li id="navbar-category-2"><a href="/book/7.html">恐怖</a></li>

<li id="navbar-category-2"><a href="/book/8.html">惊悚</a></li>

<li id="navbar-category-2"><a href="/book/9.html">历史</a></li>

<li id="navbar-category-2"><a href="/book/10.html">军事</a></li>

<li id="navbar-category-2"><a href="/book/11.html">网游</a></li>

<li id="navbar-category-2"><a href="/book/12.html">官商</a></li>

<li id="navbar-category-2"><a href="/book/13.html">评书</a></li>

<li id="navbar-category-2"><a href="/book/14.html">相声</a></li>

<li id="navbar-category-2"><a href="/book/15.html">文学</a></li>

<li id="navbar-category-2"><a href="/book/16.html">儿童</a></li>

<li id="navbar-category-2"><a href="/book/28.html">穿越</a></li>

<li id="navbar-category-2"><a href="/book/29.html">娱乐</a></li>

<li id="navbar-category-2"><a href="/book/30.html">笑话</a></li>

<li id="navbar-category-2"><a href="/book/31.html">戏曲</a></li>

<li id="navbar-category-2"><a href="/book/32.html">其它</a></li>

<li id="navbar-category-2"><a href="/book/33.html">百家讲坛</a></li>

<li><a href="https://www.52pingshu.com/">评书专区</a></li>
<li><a href="https://tingbook.cc/downapp/"><h3><span style="color: red;">APP下载</span></h3></a></li>
            </ul>
        </div>
<div class="tx-box mb10">
<div class="place f-12">当前位置：<a href='/index.html' >首页</a>&nbsp;&nbsp;&raquo;&nbsp;&nbsp;<a href='/book/1.html' >玄幻</a></div>
<ul class="row3 row-b">

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/32435.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/211214/2934c0d3b45c57a9.gif" alt="楚王妃"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 雷鬼</span><a href="/show/32435.html" class="f-bold">楚王妃</a></h2>
                                    <p class="f-gray mb10 f-12">楚王妃作者：雷鬼，由宁儿播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/32435.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/25993.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210731/bdb4a8d7dc48809e.gif" alt="绝世武神"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 亦笑天有声工作室</span><a href="/show/25993.html" class="f-bold">绝世武神</a></h2>
                                    <p class="f-gray mb10 f-12">绝世武神作者：亦笑天有声工作室，由净无痕播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/25993.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/25885.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210519/0eb6e727c9b596b2.gif" alt="大奉打更人"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 掌易灵动</span><a href="/show/25885.html" class="f-bold">大奉打更人</a></h2>
                                    <p class="f-gray mb10 f-12">大奉打更人作者：掌易灵动，由卖报小郎君播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/25885.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/25884.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="https://www.lrts5.com/uploads/allimg/210518/7505a129287c57b8.gif#err" alt="吞天"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 本良 一诺</span><a href="/show/25884.html" class="f-bold">吞天</a></h2>
                                    <p class="f-gray mb10 f-12">吞天作者：本良 一诺，由妖白菜播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/25884.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/25683.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210419/e6f00fdf9403b300.gif" alt="异世流放"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 小白 妖仙</span><a href="/show/25683.html" class="f-bold">异世流放</a></h2>
                                    <p class="f-gray mb10 f-12">异世流放作者：小白 妖仙，由易人北播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/25683.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/25666.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="https://img.iyeren.com/ximafm/uploads/allimg/210405/64dbe58b87f04daf.gif#err" alt="我有九个女徒弟"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 同桌 凌烟</span><a href="/show/25666.html" class="f-bold">我有九个女徒弟</a></h2>
                                    <p class="f-gray mb10 f-12">我有九个女徒弟作者：同桌 凌烟，由毕竟是蠢材播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/25666.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/25806.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="https://www.lrts5.com/uploads/allimg/210504/b1e615d8e02bb8b5.gif#err" alt="沧元图"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 华音传媒</span><a href="/show/25806.html" class="f-bold">沧元图</a></h2>
                                    <p class="f-gray mb10 f-12">沧元图作者：华音传媒，由我吃西红柿播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/25806.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/25645.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210316/e6098f64546c8fa3.gif" alt="元龙"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 钟健 周玢</span><a href="/show/25645.html" class="f-bold">元龙</a></h2>
                                    <p class="f-gray mb10 f-12">元龙作者：钟健 周玢，由任怨播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/25645.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/25630.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210301/069e454744191979.gif" alt="万族之劫"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 刺儿 龚玺</span><a href="/show/25630.html" class="f-bold">万族之劫</a></h2>
                                    <p class="f-gray mb10 f-12">万族之劫作者：刺儿 龚玺，由老鹰吃小鸡播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/25630.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/25613.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210220/f0142d2b0a50bc88.gif" alt="我师兄实在太稳健了"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 墨客 伽蛮菌</span><a href="/show/25613.html" class="f-bold">我师兄实在太稳健了</a></h2>
                                    <p class="f-gray mb10 f-12">我师兄实在太稳健了作者：墨客 伽蛮菌，由言归正传播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/25613.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/25088.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/201225/e61b37703c6e71fe.gif" alt="绝世武魂"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 领先声创</span><a href="/show/25088.html" class="f-bold">绝世武魂</a></h2>
                                    <p class="f-gray mb10 f-12">绝世武魂作者：领先声创，由洛城东播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/25088.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/25087.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/201225/462aa1b81c0a6ae0.gif" alt="斗罗大陆4终极斗罗"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 骤雨惊弦</span><a href="/show/25087.html" class="f-bold">斗罗大陆4终极斗罗</a></h2>
                                    <p class="f-gray mb10 f-12">斗罗大陆4终极斗罗作者：骤雨惊弦，由唐家三少播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/25087.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/25138.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/201225/3e7eb470e73ffcc6.gif" alt="九转道经"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 壮则思飞</span><a href="/show/25138.html" class="f-bold">九转道经</a></h2>
                                    <p class="f-gray mb10 f-12">九转道经作者：壮则思飞，由天茗播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/25138.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/25128.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/201225/aebb8251df902742.gif" alt="九星霸体诀"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 舟扬</span><a href="/show/25128.html" class="f-bold">九星霸体诀</a></h2>
                                    <p class="f-gray mb10 f-12">九星霸体诀作者：舟扬，由平凡魔术师播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/25128.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/25958.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210629/1a5a6d9b6b87e5d9.gif" alt="神魔天尊"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 丹羽道 浥轻尘 曉夢</span><a href="/show/25958.html" class="f-bold">神魔天尊</a></h2>
                                    <p class="f-gray mb10 f-12">神魔天尊作者：丹羽道 浥轻尘 曉夢，由九当家播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/25958.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

                    <li class="col-12 col-m-24 col3-">
        <div class="style-img clearfix">
            <a href="/show/25634.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210308/99fc1fa1506d6510.gif" alt="神魂丹帝"></span></a>
            <section>
                <h2 class="style-title txt-ov f-15 mb5"><span class="fr f-12 f-gray"><i class="iconfont icon-user"></i> 果维听书</span><a href="/show/25634.html" class="f-bold">神魂丹帝</a></h2>
                                    <p class="f-gray mb10 f-12">神魂丹帝作者：果维听书，由浊酒一湖播音，听书网有声小说提供收听平台，欢迎你到本站收听节目，本站不间断收录最新小说，希望你能喜欢！</p>
                <p><a href="/show/25634.html" class="style-btn tx-c1">开始收听</a></p>
            </section>
        </div>
    </li>

        </ul>
</div>

<div class="pagebar ta-c mb15"><span>
        <a href="/book/1.html"><span class="page">首页</span></a>
        <a href="/book/1-0.html" ><span class="page">‹‹</span></a>

            <span class="page now-page">1</span>

            <a href="/book/1-2.html" ><span class="page">2</span></a>

            <a href="/book/1-2.html" ><span class="page">››</span></a>
        <a href="/book/1-113.html"><span class="page">尾页</span></a>
        </span>
</div>




<div class="footer ta-c f-12">
<a href="" target="_blank" title="关于我们">关于我们</a> - <a href="/gbook.php" target="_blank" title="投诉举报">投诉举报</a> - <a href="/gbook.php" target="_blank" title="留言反馈">留言反馈</a> - <a href="/xml/baidu.xml" target="_blank" title="网站地图">网站地图</a><br><br>免责声明：本站资源来源于网络，版权归原作者所有，若有侵犯您的权利，请来信告知，我们将立即予以删除。！<br>
<p>Powered By <a href="/" title="听书网" target="_blank">听书网--邮箱：5261287@qq.com</a>
<script>
var _hmt = _hmt || [];
(function() {
var hm = document.createElement("script");
hm.src = "https://hm.baidu.com/hm.js?2b17643065761366d8a45ded7a8f69cf";
var s = document.getElementsByTagName("script")[0];
s.parentNode.insertBefore(hm, s);
})();
</script>
</p>
Copyright Your WebSite.Some Rights Reserved.</div>
</div>
<div class="nav-off"></div>
<div class="gotop tx-color"><i class="iconfont icon-caret-up"></i></div>

<div class="side-gg gg-box side1"><a href="#"><img src="/templets/tingshu/images/gg2.jpg"></a><a href="javascript:;" class="gg-off"><i class="iconfont icon-close-circle"></i></a></div>
<div class="side-gg gg-box side2"><a href="#"><img src="/templets/tingshu/images/gg2.jpg"></a><a href="javascript:;" class="gg-off"><i class="iconfont icon-close-circle"></i></a></div>
<script src="/templets/tingshu/images/txcstx.js"></script>

</body>
</html>
"""
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

endpage_url = '/book/10-9.html'
categoryid = int(re.findall(r'/(\d+)-', endpage_url)[0])
print(categoryid)


