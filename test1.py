import re
# import util

# a = "google Runoob Taobaoa119?"
# print(a)
# html_str = re.findall(r""" [aeiou] """, a, re.VERBOSE | re.DOTALL)  # 匹配 字符串a中的所有 a e i o u字符
# print(html_str)
# html_str = re.findall(r""" [^aeiou] """, a, re.VERBOSE | re.DOTALL)  # 非[...] 里的所有字符
# print(html_str)
# html_str = re.findall(r""" [A-Z] """, a, re.VERBOSE | re.DOTALL)  # 所有大写字母
# print(html_str)
# html_str = re.findall(r""" [\w] """, a, re.VERBOSE | re.DOTALL)  # 匹配 字母、数字、下划线。等价于[A-Za-z0-9]
# print(html_str)
# html_str = re.findall(r""" \w """, a, re.VERBOSE | re.DOTALL)  # 匹配 字母、数字、下划线。等价于[A-Za-z0-9_], 不写[]的格式，建议带[]
# print(html_str)
# html_str = re.findall(r""" . """, a, re.VERBOSE | re.DOTALL)  # 匹配 除换行符（\n \r)之外的任何单个字符。等价于[^\n\r]。此符号不带[]
# print(html_str)
# html_str = re.findall(r""" [\s\S] """, a, re.VERBOSE | re.DOTALL)  # 匹配 所有。\s 是匹配所有空白符，包括换行，\S 非空白符，不包括换行
# print(html_str)
# html_str = re.findall(r""" \w""", a, re.VERBOSE | re.DOTALL)  # 匹配 字母数字下划线
# print(html_str)


# chapter
html_str = """

<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="renderer" content="webkit">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>楚王妃有声小说_001.mp3_听书网官网_天天在线听书网56_有声小说网_听书网有声小说</title>
<meta name="Keywords"content="楚王妃有声小说,楚王妃有声小说在线收听,在线听书网,有声小说网,听书网有声小说"/>
<meta name="description"content="正在收听楚王妃有声小说001.mp3,楚王妃有声小说,在线听书网,有声小说网,听书网有声小说,欢迎各位听友收听《楚王妃》."/>
        <link href="/templets/tingshu/images/favicon_tx.ico" type="image/x-icon" rel="icon"/>
        <link rel="stylesheet" rev="stylesheet" href="/templets/tingshu/images/iconfont.css" type="text/css" media="all" />
        <link rel="stylesheet" rev="stylesheet" href="/templets/tingshu/images/shiui.min.css" type="text/css" media="all" />
        <link rel="stylesheet" rev="stylesheet" href="/templets/tingshu/images/txcstx.css" type="text/css" media="all" />
<script type="text/javascript" src="/js/common.js"></script>
<script type="text/javascript" src="/js/function.js"></script>
<script type="text/javascript">var sitePath='', siteUrl='http://www.tingbook.cc'</script>
        <script type="text/javascript" src="/js/play.js"></script>
		<script type="text/javascript">var playn='楚王妃', playp='001.mp3';</script>
		<script type="text/javascript">var vod_name='楚王妃',vod_url=window.location.href,vod_part='001.mp3';</script>
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
            <div id="txtbox1" class="tx-box mb10">
    <div class="place f-12">当前位置：<a href='/index.html' >首页</a>&nbsp;&nbsp;&raquo;&nbsp;&nbsp;<a href='/book/1.html' >玄幻</a>&nbsp;&nbsp;&raquo;&nbsp;&nbsp;<a href='/show/32435.html'>楚王妃</a></div>
        <div class="info-title ta-c pd15">
    <h1 class="f-22 mb10">楚王妃001.mp3 </h1>
    <p class="f-12"><span class="mr15">作者：<a href='/search.php?searchword=%E9%9B%B7%E9%AC%BC'>雷鬼</a>&nbsp;&nbsp;</span> <span class="mr15">播音：<a href='/search.php?searchword=%E5%AE%81%E5%84%BF'>宁儿</a>&nbsp;&nbsp;</span><span class="mr15">收听：<span id="hit">加载中...</span><script>getVideoHit('32435')</script></span></p>
</div>
<div class="gg-box pd15-2"><a href="#"><img src="/templets/tingshu/images/gg1.jpg"></a></div>
<div id="txtbox" class="tx-text pd15">
<script>var vid="32435";var vfrom="0";var vpart="0";var now="https://t3344t.tingchina.com/yousheng/玄幻奇幻/楚王妃/001.mp3";var pn="jplayer"; var next="https://t3344t.tingchina.com/yousheng/玄幻奇幻/楚王妃/002.mp3";var prePage="/jpplay/32435-0-0.html";var nextPage="/jpplay/32435-0-1.html";</script><iframe id='cciframe' scrolling='no' frameborder='0' allowfullscreen></iframe><script>var pn=pn;var forcejx1=forcejx;var forcejx2="no";var forcejx3=forcejx;if(forcejx1!=forcejx2 && contains(unforcejxARR,pn)==false){pn=forcejx3;}else{pn=pn;}document.getElementById("cciframe").width = playerw;document.getElementById("cciframe").height = playerh;document.getElementById("cciframe").src = '/js/player/'+ pn + '.html';</script>
</div>

<div class="info-next ta-c pd15-2">
        <a href="/show/32435.html" class="cateurl">章节目录</a>
    <a href="/jpplay/32435-0-1.html" class="nexturl on">下一章</a></div>
<p class="f-12 ta-c f-gray pd15">小技巧：按 Ctrl+D 快速保存当前章节页面至浏览器收藏夹；按 回车[Enter]键 返回章节目录，按 ←键 回到上一章，按 →键 进入下一章。</p>


<script language="javaScript">
    $(document).keydown(function(event){
        if(event.keyCode == 13){window.location.href = $(".cateurl").attr('href');return;}
        if(event.keyCode == 37){if($(".preurl").hasClass("on")){window.location.href = $(".preurl").attr('href');}else{alert('你看的正是第一章！');}}
        if(event.keyCode == 39){if($(".nexturl").hasClass("on")){window.location.href = $(".nexturl").attr('href');}else{alert('你已经全部看完了，请等待作者更新');}}
    });
</script>     </div>

<div class="tx-box mb10">
    <div class="tx-comments">
<div  id="comment_list">评论加载中...</div><script>viewComment("/comment.php?id=32435&type=0","")</script>
</div>
</div>
<div class="row2">
                           <dl class="col-24 col-m-24 col2- mb10">
        <dd class="tx-box">
            <h2 class="tx-title1 f-15"><strong>猜你喜欢</strong></h2>
            <div class="pd10-3">
                <ul class="row1">

                                                                                <li class="col-6 col-m-24 col1- mb10">
                    <div class="style-img clearfix">
                        <a href="/show/25885.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210519/0eb6e727c9b596b2.gif" alt="大奉打更人"></span></a>
                        <section>
                            <h2 class="style-title txt-ov f-15 mb5"><span class="f-12 fr f-gray"><i class="iconfont icon-user"></i> <a href='/search.php?searchword=%E6%8E%8C%E6%98%93%E7%81%B5%E5%8A%A8'>掌易灵动</a>&nbsp;</span><a href="/show/25885.html" class="f-bold">大奉打更人</a></h2>
                            <p class="mb5 f-12"><a href="/book/1.html" class="tx-c1">玄幻</a> </p>                            <p class="f-gray mb10 f-12">大奉打更人作者：掌易灵动，由卖报小郎君播音。</p>
                            <p><a href="/show/25885.html" class="style-btn tx-c1">开始收听</a> </p>
                        </section>
                    </div>
                    </li>

                                                                                <li class="col-6 col-m-24 col1- mb10">
                    <div class="style-img clearfix">
                        <a href="/show/15227.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/191209/cf2d76e311c6c50a.jpg" alt="黄金瞳（郭益达）"></span></a>
                        <section>
                            <h2 class="style-title txt-ov f-15 mb5"><span class="f-12 fr f-gray"><i class="iconfont icon-user"></i> <a href='/search.php?searchword=%E6%89%93%E7%9C%BC'>打眼</a>&nbsp;</span><a href="/show/15227.html" class="f-bold">黄金瞳（郭益达）</a></h2>
                            <p class="mb5 f-12"><a href="/book/1.html" class="tx-c1">玄幻</a> </p>                            <p class="f-gray mb10 f-12">黄金瞳（郭益达）作者：打眼，由郭益达播音。</p>
                            <p><a href="/show/15227.html" class="style-btn tx-c1">开始收听</a> </p>
                        </section>
                    </div>
                    </li>

                                                                                <li class="col-6 col-m-24 col1- mb10">
                    <div class="style-img clearfix">
                        <a href="/show/25638.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/210310/990769cffbda31a5.gif" alt="全职法师"></span></a>
                        <section>
                            <h2 class="style-title txt-ov f-15 mb5"><span class="f-12 fr f-gray"><i class="iconfont icon-user"></i> <a href='/search.php?searchword=%E6%A2%A6%E6%B8%B8%E6%96%B0%E5%A3%B0'>梦游新声</a>&nbsp;</span><a href="/show/25638.html" class="f-bold">全职法师</a></h2>
                            <p class="mb5 f-12"><a href="/book/1.html" class="tx-c1">玄幻</a> </p>                            <p class="f-gray mb10 f-12">全职法师作者：梦游新声，由乱播音。</p>
                            <p><a href="/show/25638.html" class="style-btn tx-c1">开始收听</a> </p>
                        </section>
                    </div>
                    </li>

                                                                                <li class="col-6 col-m-24 col1- mb10">
                    <div class="style-img clearfix">
                        <a href="/show/27024.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/211111/36adaa18d382127b.gif" alt="斗破苍穹"></span></a>
                        <section>
                            <h2 class="style-title txt-ov f-15 mb5"><span class="f-12 fr f-gray"><i class="iconfont icon-user"></i> <a href='/search.php?searchword=%E8%9C%A1%E7%AC%94%E5%B0%8F%E5%8B%87'>蜡笔小勇</a>&nbsp;<a href='/search.php?searchword=%E8%8E%9C%E5%84%BF'>莜儿</a>&nbsp;</span><a href="/show/27024.html" class="f-bold">斗破苍穹</a></h2>
                            <p class="mb5 f-12"><a href="/book/1.html" class="tx-c1">玄幻</a> </p>                            <p class="f-gray mb10 f-12">斗破苍穹作者：蜡笔小勇 莜儿，由天蚕土豆播音。</p>
                            <p><a href="/show/27024.html" class="style-btn tx-c1">开始收听</a> </p>
                        </section>
                    </div>
                    </li>

                                                                                <li class="col-6 col-m-24 col1- mb10">
                    <div class="style-img clearfix">
                        <a href="/show/25103.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/201225/9ca2b04f3e52e1f8.gif" alt="大王饶命"></span></a>
                        <section>
                            <h2 class="style-title txt-ov f-15 mb5"><span class="f-12 fr f-gray"><i class="iconfont icon-user"></i> <a href='/search.php?searchword=%E5%88%BA%E5%84%BF'>刺儿</a>&nbsp;<a href='/search.php?searchword=%E5%85%AB%E9%9F%B3%E5%85%AD%E5%90%88'>八音六合</a>&nbsp;</span><a href="/show/25103.html" class="f-bold">大王饶命</a></h2>
                            <p class="mb5 f-12"><a href="/book/1.html" class="tx-c1">玄幻</a> </p>                            <p class="f-gray mb10 f-12">大王饶命作者：刺儿 八音六合，由会说话的肘子播音。</p>
                            <p><a href="/show/25103.html" class="style-btn tx-c1">开始收听</a> </p>
                        </section>
                    </div>
                    </li>

                                                                                <li class="col-6 col-m-24 col1- mb10">
                    <div class="style-img clearfix">
                        <a href="/show/25098.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/201225/2395cf490c853c89.gif" alt="凡人修仙传之仙界篇"></span></a>
                        <section>
                            <h2 class="style-title txt-ov f-15 mb5"><span class="f-12 fr f-gray"><i class="iconfont icon-user"></i> <a href='/search.php?searchword=%E5%A4%A7%E7%81%B0%E7%8B%BC'>大灰狼</a>&nbsp;</span><a href="/show/25098.html" class="f-bold">凡人修仙传之仙界篇</a></h2>
                            <p class="mb5 f-12"><a href="/book/1.html" class="tx-c1">玄幻</a> </p>                            <p class="f-gray mb10 f-12">凡人修仙传之仙界篇作者：大灰狼，由忘语播音。</p>
                            <p><a href="/show/25098.html" class="style-btn tx-c1">开始收听</a> </p>
                        </section>
                    </div>
                    </li>

                                                                                <li class="col-6 col-m-24 col1- mb10">
                    <div class="style-img clearfix">
                        <a href="/show/25134.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/201225/8c64f7d3e421e29b.gif" alt="元尊"></span></a>
                        <section>
                            <h2 class="style-title txt-ov f-15 mb5"><span class="f-12 fr f-gray"><i class="iconfont icon-user"></i> <a href='/search.php?searchword=%E5%88%BA%E5%84%BF'>刺儿</a>&nbsp;</span><a href="/show/25134.html" class="f-bold">元尊</a></h2>
                            <p class="mb5 f-12"><a href="/book/1.html" class="tx-c1">玄幻</a> </p>                            <p class="f-gray mb10 f-12">元尊作者：刺儿，由天蚕土豆播音。</p>
                            <p><a href="/show/25134.html" class="style-btn tx-c1">开始收听</a> </p>
                        </section>
                    </div>
                    </li>

                                                                                <li class="col-6 col-m-24 col1- mb10">
                    <div class="style-img clearfix">
                        <a href="/show/26093.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/211111/d5ec0fc8f041af1b.gif" alt="星辰变"></span></a>
                        <section>
                            <h2 class="style-title txt-ov f-15 mb5"><span class="f-12 fr f-gray"><i class="iconfont icon-user"></i> <a href='/search.php?searchword=%E5%8E%9F%E9%87%8E'>原野</a>&nbsp;</span><a href="/show/26093.html" class="f-bold">星辰变</a></h2>
                            <p class="mb5 f-12"><a href="/book/1.html" class="tx-c1">玄幻</a> </p>                            <p class="f-gray mb10 f-12">星辰变作者：原野，由我吃西红柿播音。</p>
                            <p><a href="/show/26093.html" class="style-btn tx-c1">开始收听</a> </p>
                        </section>
                    </div>
                    </li>

                                                                                <li class="col-6 col-m-24 col1- mb10">
                    <div class="style-img clearfix">
                        <a href="/show/25104.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/201225/31027c6f6faf28ac.gif" alt="诡秘之主"></span></a>
                        <section>
                            <h2 class="style-title txt-ov f-15 mb5"><span class="f-12 fr f-gray"><i class="iconfont icon-user"></i> <a href='/search.php?searchword=%E6%A2%93%E8%BE%B0'>梓辰</a>&nbsp;<a href='/search.php?searchword=%E7%BC%88%E7%BC%88'>缈缈</a>&nbsp;</span><a href="/show/25104.html" class="f-bold">诡秘之主</a></h2>
                            <p class="mb5 f-12"><a href="/book/1.html" class="tx-c1">玄幻</a> </p>                            <p class="f-gray mb10 f-12">诡秘之主作者：梓辰 缈缈，由爱潜水的乌贼播音。</p>
                            <p><a href="/show/25104.html" class="style-btn tx-c1">开始收听</a> </p>
                        </section>
                    </div>
                    </li>

                                                                                <li class="col-6 col-m-24 col1- mb10">
                    <div class="style-img clearfix">
                        <a href="/show/32435.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/211214/2934c0d3b45c57a9.gif" alt="楚王妃"></span></a>
                        <section>
                            <h2 class="style-title txt-ov f-15 mb5"><span class="f-12 fr f-gray"><i class="iconfont icon-user"></i> <a href='/search.php?searchword=%E9%9B%B7%E9%AC%BC'>雷鬼</a>&nbsp;</span><a href="/show/32435.html" class="f-bold">楚王妃</a></h2>
                            <p class="mb5 f-12"><a href="/book/1.html" class="tx-c1">玄幻</a> </p>                            <p class="f-gray mb10 f-12">楚王妃作者：雷鬼，由宁儿播音。</p>
                            <p><a href="/show/32435.html" class="style-btn tx-c1">开始收听</a> </p>
                        </section>
                    </div>
                    </li>

                                                                                <li class="col-6 col-m-24 col1- mb10">
                    <div class="style-img clearfix">
                        <a href="/show/25108.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/201225/f00072ea0c5648ce.gif" alt="全球高武"></span></a>
                        <section>
                            <h2 class="style-title txt-ov f-15 mb5"><span class="f-12 fr f-gray"><i class="iconfont icon-user"></i> <a href='/search.php?searchword=%E5%85%B3%E5%BD%A6%E4%B9%8B'>关彦之</a>&nbsp;</span><a href="/show/25108.html" class="f-bold">全球高武</a></h2>
                            <p class="mb5 f-12"><a href="/book/1.html" class="tx-c1">玄幻</a> </p>                            <p class="f-gray mb10 f-12">全球高武作者：关彦之，由老鹰吃小鸡播音。</p>
                            <p><a href="/show/25108.html" class="style-btn tx-c1">开始收听</a> </p>
                        </section>
                    </div>
                    </li>

                                                                                <li class="col-6 col-m-24 col1- mb10">
                    <div class="style-img clearfix">
                        <a href="/show/25120.html" class="img-80 fl mr15"><span class="img-box" data-ratio="16:20"><img src="/uploads/allimg/201225/0da7705c882abc58.gif" alt="三界红包群"></span></a>
                        <section>
                            <h2 class="style-title txt-ov f-15 mb5"><span class="f-12 fr f-gray"><i class="iconfont icon-user"></i> <a href='/search.php?searchword=%E8%9B%90%E8%9B%90'>蛐蛐</a>&nbsp;<a href='/search.php?searchword=%E6%80%9D%E4%BA%88%E7%94%9C'>思予甜</a>&nbsp;</span><a href="/show/25120.html" class="f-bold">三界红包群</a></h2>
                            <p class="mb5 f-12"><a href="/book/1.html" class="tx-c1">玄幻</a> </p>                            <p class="f-gray mb10 f-12">三界红包群作者：蛐蛐 思予甜，由小教主播音。</p>
                            <p><a href="/show/25120.html" class="style-btn tx-c1">开始收听</a> </p>
                        </section>
                    </div>
                    </li>

                                                        </ul>
            </div>
        </dd>
    </dl>
    	<div class="row2">
     <dl class="col-24 col-m-24 col2- mb10">
        <dd class="tx-box">
				<h2 class="tx-title2 f-15"><strong>
					友情链接：
				</strong></h2>
				     <ul class="ul-36 ul-b ul-home-new pd10-4">
				<a href="https://tingbook.cc/">有声小说</a> | <a href="https://tingbook.cc/">天天听书</a> | <a href="https://tingbook.cc/">520听书网</a> | <a href="https://www.hj8.org/">韩剧吧</a> | <a href="https://www.fzdm.org/">风之动漫</a> | <a href="https://52pingshu.com">我爱评书网</a>
				</ul>
				    </dl>
            </div>

<!-- 友链 -->
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

# cbrbms = re.findall(r""".+?cbrbm":"(.+?)"
#     .+?cbrmc":"(.+?)"
#     """, html_str, re.VERBOSE | re.DOTALL)
# now = re.findall(r""" .*?var now=.*? """, html_str, re.VERBOSE | re.DOTALL)
# now = re.findall(r""" http://audio.xmcdn.com/group13/M02/68/74/wKgDXlXkcIOxPJABAJZAqURUajY488.m4a """, html_str, re.VERBOSE | re.DOTALL)
# now = re.findall(r'var\s now=".+?mp3', html_str, re.VERBOSE | re.DOTALL)
# now = re.findall(r'var\s now=.+?mp3', html_str)
# print(now)
# strlist = re.findall(r'(?<=var\snow=").*?mp3', html_str, re.VERBOSE | re.DOTALL)
strlist = re.findall(r'var\s now="(.+?)";', html_str, re.VERBOSE | re.DOTALL)[0]
print(strlist)
# util.create_thrads_by_class_thread()


# 2个字符之间的内容
# str = 'a123b'
# print(re.findall(r'a(.+?)b', str))

# util.fun1()
# thread1 = threading.Thread(dbutil.print_cfg())  # target= 方法名加不加括号都可用,我一般加上
# thread1.start()


#  获取章节 media
# now = re.findall('(?<=com/).*$', "www.example.com/thedubaimall")
# print(now)
# re.findall('(?<=com).*$', "www.example.com/thedubaimall")

