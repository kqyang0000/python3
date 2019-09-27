# coding=utf-8

from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('<%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html><head>
            <meta charset="UTF-8">
                          <title>首页</title>
                                     <base target="_self">
                                                  <link href="/framework-web/static/images/logo1.png" rel="shortcut icon">
                                                                                                          <link href="/framework-web/static/css/index.css" rel="stylesheet">
                                                                                                                                                               <link href="/framework-web/static/css/jquery.gridster.css" rel="stylesheet">
                                                                                                                                                                                                                              <link rel="stylesheet" type="text/css" href="/framework-web/static/bootstrap/css/bootstrap.css">
                                                                                                                                                                                                                                                                          <link href="/framework-web/static/icon-menu/iconfont.css" rel="stylesheet">
                                                                                                                                                                                                                                                                                                                                        <link href="/framework-web/static/css/menu.css" rel="stylesheet">
                                                                                                                                                                                                                                                                                                                                                                                            <!-- 湖南初始样式 -->
<link id="qh" href="/framework-web/static/css/light-shallowblue.css" rel="stylesheet">
                                                                         <link id="themes" rel="stylesheet" type="text/css" href="/framework-web/static/easyui/themes/bootstrap/easyui.css">
                                                                                                                                 </head>
                                                                                                                                   <body class="show_page" style="">
<!-- 消息弹框 -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
<div class="qqBox">
<div class="boxHead">
<div class="internetName">消息</div>
<div class="headName"></div>
<button type="button" class="close" style="float:right" data-dismiss="modal" aria-hidden="true">×</button>
</div>
<div class="context">
<div class="conLeft">
<!--搜索框-->
<form action="#" id="search_box">
<div class="wrapper">
<input id="search" type="text" name="search" placeholder="搜索"><button type="submit" class="search_btn">搜索</button>
</div>
</form>
<!--用户列表-->
<img src="grp/easyui/common/images/reloading.gif" id="userinfo" style="display: none;">
<ul id="user1"></ul>
</div>
<div class="conRight">
<div class="rightCont">
<div class="chatRecord">查看更多消息</div>
<ul id="mess1" class="newsList"></ul>
</div>
<div class="rightFoot">
<div class="footTop">
<span id="pic" onclick="upload()" class="glyphicon glyphicon-folder-open" aria-hidden="true"></span>
</div>
<div class="inputBox">
<form id="impForm" method="post" enctype="multipart/form-data">
<input id="file_" style="display:none" name="file" type="file" accept="application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-powerpoint,application/vnd.openxmlformats-officedocument.presentationml.presentation,text/plain,application/pdf" multiple="">
</form>
<textarea id="dope" autofocus="autofocus" name="" rows="" cols=""></textarea>
<button class="sendBtn">发送(s)</button>
</div>
</div>
</div>
</div>
</div>
</div>
<!-- 修改密码模态框 -->
<div class="modal fade" id="myModal2" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
<iframe frameborder="0" allowtransparency="true" scrolling="no" style="background-color:transparent; position: absolute; z-index: -1; width: 100%; height: 100%; top: 0;left:0;"></iframe>
<div class="modal-dialog" style="width:440px;">
<div class="modal-content" style="margin-top:180px;">
<div class="modal-header">
<button type="button" class="close" data-dismiss="modal" aria-hidden="true">
×
</button>
<h4 class="modal-title" id="myModalLabel">
修改密码
</h4>
</div>
<div class="modal-body">
<form id="loginform" class="form-horizontal" role="form">
<div class="form-group">
<label for="firstname" class="col-sm-3 control-label">初始密码：</label>
<div class="col-sm-9">
<input type="password" name="pass1" id="pass1" class="form-control" placeholder="请输入初始密码">
</div>
</div>
<div class="form-group">
<label for="lastname" class="col-sm-3 control-label">新密码：</label>
<div class="col-sm-9">
<input type="password" name="pass2" id="pass2" class="form-control" placeholder="请输入新密码">
</div>
</div>
<div class="form-group">
<label for="lastname" class="col-sm-3 control-label">确认新密码</label>
<div class="col-sm-9">
<input type="password" name="pass3" id="pass3" class="form-control" placeholder="请再次输入新密码">
</div>
</div>
</form>
<div id="tip1" class="alert alert-danger hide" style="width:400px;height:40px;margin-bottom:0;text-align:center;line-height:20px;margin-left:10px;padding:10px 0;" role="alert"></div>
<div id="tip2" class="alert alert-success hide" style="width:400px;height:40px;margin-bottom:0;text-align:center;line-height:20px;margin-left:10px;padding:10px 0;" role="alert"></div>
</div>
<div class="modal-footer">
<button type="button" class="btn btn-primary" onclick="login1()" style="height:21px;width:50px;line-height:21px;padding:0;border-radius:0;font-size:12px;">
确认
</button>
<button type="button" class="btn btn-default" data-dismiss="modal" style="height:21px;width:50px;line-height:21px;padding:0;border-radius:0;font-size:12px;">
关闭
</button>
</div>
</div>
</div>
</div>
<!--Top导航条-->
<div id="menu-wrap">
<ul id="menu-left">
<li class="logo-pic">
<a href="javascript:void(0);">
<span class="glyphicon glyphicon-menu-hamburger"><img class="logo-img" style="display:none;width:20px;height:20px;" src=""></span>
</a>
</li>
<li class="logo-area" id="zh1">湖南电子财政一体化系统</li>
</ul>
<ul id="menu-right">
<li id="code11"><a href="javascript:void(0);" id="a1">admin</a></li>
<li id="user12"><a href="javascript:void(0);" id="a2">湖南电子财政</a></li>
<li id="area"><a href="javascript:void(0);"></a></li>
<li id="year">
<div class="drop-box">
<div class="books-year drop-year">2020</div>
<div class="item-wrap item-year" id="year1"><li value="2020">2020</li></div>
</div>
</li>
<li id="books">
<div class="drop-box">
<div class="books-year drop-book" id="zt2">...</div>
<span onclick="navBooksItem()" class="glyphicon glyphicon-menu-down" aria-hidden="true"></span>
<div class="item-wrap item-book" id="books1"><li value=""></li></div>
</div>
</li>
<li class="user-info" style="z-index:5">
<a href="javascript:void(0);">
<span class="glyphicon glyphicon-user" aria-hidden="true"></span>
</a>
<ul>
<li class="user-code">
<span class="glyphicon glyphicon-user code1" aria-hidden="true">&nbsp;用户编码：</span>
<span id="ucode" title="admin">admin</span>
<label><input id="checkbox1" type="checkbox" onclick="yhcode(this)">显示在导航栏</label>
</li>
<li>
<span class="user11">用户信息：</span>
<span id="userinfo1" title="湖南电子财政">湖南电子财政</span>
<label><input id="checkbox2" type="checkbox" onclick="yhinfo(this)">显示在导航栏</label>
</li>
<li class="financial">
<span class="ssjg">所属机构：</span>
<span class="financial-area"></span>
<label><input id="cz" type="checkbox" onclick="FinancialArea(this)">显示在导航栏</label>
</li>
<li class="financial-year">
<span style="float: left;">当前年度：</span>
<div class="drop-box" id="">
<div class="books-year drop-year" id="">2020</div>
<div id="xl1"><div class="books-year drop-year" ztid="2020">2020</div><div class="books-year drop-year" ztid="2019">2019</div></div>
<span onclick="myYearItem()" class="glyphicon glyphicon-menu-down" aria-hidden="true"></span>
<div class="item-wrap item-year"><li value="2020">2020</li></div>

</div>
<label><input id="nd" type="checkbox" onclick="CurrentYear(this)">显示在导航栏</label>
</li>
<li class="financial-books">

<span style="float: left;">当前账套：</span>
<div class="drop-box" id="zt">
<div class="books-year drop-book" id="yb">...</div>
<div id="xl"></div>
<span onclick="myBooksItem()" class="glyphicon glyphicon-menu-down" aria-hidden="true"></span>
<div class="item-wrap item-book"><li value=""></li></div>
</div>
<label><input id="zt1" type="checkbox" onclick="CurrentBooks(this)">显示在导航栏</label>
</li>
<li>
<span>当前主题</span>
<div class="themeBox" style="display:inline-block;">
<button class="skin-btn shallowblue" value="shallowblue"></button>
</div>
</li>
<li class="roles">
<div class="user_name">用户角色：</div>
<div id="user_role" style="line-height: 40px;">湖南省财政厅系统管理员</div>
</li>
<li class="sign-out"><a onclick="btna()" href="javascript:void(0);">密码设置</a></li>
<li class="sign-out"><a onclick="logout(this)" href="javascript:void(0);">退出登录</a></li>
<iframe frameborder="0" allowtransparency="true" scrolling="no" style="background-color:transparent; position: absolute; z-index: -1; width: 100%; height: 100%; top: 0;right:0;"></iframe>
</ul>
</li>
</ul>
</div>
<!-- Left导航-湖南 -->
<ul class="mune-icon sec hunan-left">
<li title="菜单闭合" class="fold"><a href="javascript:void(0)"></a></li>
<li title="全部菜单" class="change-color" totalmenu="0" id="menusTotal"><a href="javascript:void(0)"></a></li>
<!-- <li title="待办事项"><a href="javascript:void(0)"></a></li> -->
<!-- <li title="常用菜单"><a href="javascript:void(0)"></a></li> -->
<!-- <li title="最近访问"><a href="javascript:void(0)"></a></li> -->
<!--  <li title="我的消息" class="menu-news"><a href="javascript:void(0)"></a></li> -->
<!-- <li title="我的报表"><a href="javascript:void(0)"></a></li> -->
<!--  <li title="业务引导"><a href="javascript:void(0)"></a></li> -->
</ul>
<!-- menu左侧菜单 -->
<div class="menuWrap">
<div class="oneLevel">
<ul><li><a href="javascript:void(0)">系统配置</a></li></ul>
</div>
<!-- 二级三级菜单结构 -->
<!-- <div class="otherLevel">
<ul class="twoLevel">
<li>
<a href="javascript:void(0)">收入登记<i></i></a>
<ul class="threeLevel">
<li>
<a href="javascript:void(0)">部门标识</a>
</li>
</ul>
</li>
</ul>
</div>-->
<!-- 加载中loading -->
<div class="menuLoading" style="display: none;">
<img src="grp/easyui/common/images/reloading.gif">
</div>
<div class="otherLevel"><ul class="twoLevel"><li class="active" customid="10009616" opentype="0" customurl="" customname="用户及应用门户"><a href="javascript:void(0)">用户及应用门户<i></i></a><ul class="threeLevel"><li customid="10009622" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/user_managers&amp;menuid=10009622" customname="用户管理(关联角色)"><a href="javascript:void(0)">用户管理(关联角色)</a></li><li customid="10009617" opentype="0" customurl="/portal-web/ctjview?path=grp/pt/common/html/portal_component_manager&amp;menuid=10009617" customname="门户组件管理"><a href="javascript:void(0)">门户组件管理</a></li><li customid="10009618" opentype="0" customurl="/portal-web/ctjview?path=grp/pt/common/html/home_plan&amp;menuid=10009618" customname="门户组件方案"><a href="javascript:void(0)">门户组件方案</a></li><li customid="10009619" opentype="0" customurl="/portal-web/ctjview?path=grp/pt/common/html/subsystemRegist&amp;menuid=10009619" customname="子系统注册"><a href="javascript:void(0)">子系统注册</a></li><li customid="10009620" opentype="0" customurl="/portal-web/ctjview?path=grp/pt/common/html/portalRoleManagers&amp;menuid=10009620" customname="角色管理（子系统授权）"><a href="javascript:void(0)">角色管理（子系统授权）</a></li><li customid="10009621" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/organizational_maintenance&amp;menuid=10009621" customname="所辖组织机构管理"><a href="javascript:void(0)">所辖组织机构管理</a></li><li customid="10009623" opentype="0" customurl="/portal-web/ctjview?path=grp/pt/common/html/rules_upload&amp;menuid=10009623" customname="政策法规上传"><a href="javascript:void(0)">政策法规上传</a></li><li customid="10009624" opentype="0" customurl="/portal-web/ctjview?path=grp/pt/common/html/announceNews&amp;menuid=10009624" customname="消息公告发布"><a href="javascript:void(0)">消息公告发布</a></li><li customid="10009625" opentype="0" customurl="/portal-web/ctjview?path=grp/pt/common/html/file_upload&amp;menuid=10009625" customname="文件上传"><a href="javascript:void(0)">文件上传</a></li></ul></li><li class="" customid="10009626" opentype="0" customurl="" customname="用户及系统界面方案"><a href="javascript:void(0)">用户及系统界面方案<i></i></a><ul class="threeLevel"><li customid="10009634" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/user_managers&amp;menuid=10009634" customname="用户管理(角色授权)"><a href="javascript:void(0)">用户管理(角色授权)</a></li><li customid="10009627" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/role_managers&amp;menuid=10009627" customname="角色管理(功能、用户授权)"><a href="javascript:void(0)">角色管理(功能、用户授权)</a></li><li customid="10009628" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/common_fun&amp;menuid=10009628" customname="常用功能管理"><a href="javascript:void(0)">常用功能管理</a></li><li customid="10009629" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/menu_plan&amp;menuid=10009629" customname="全部菜单管理"><a href="javascript:void(0)">全部菜单管理</a></li><li customid="10009630" opentype="0" customurl="/userportal-web/ctjview?path=grp/pt/common/html/home_plan&amp;menuid=10009630" customname="首页组件管理"><a href="javascript:void(0)">首页组件管理</a></li><li customid="10009631" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/business_configure&amp;menuid=10009631" customname="业务引导管理"><a href="javascript:void(0)">业务引导管理</a></li><li customid="10009632" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/sysMessageModify&amp;menuid=10009632" customname="系统信息修改(名称、logo)"><a href="javascript:void(0)">系统信息修改(名称、logo)</a></li><li customid="10009633" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/organizational_maintenance&amp;menuid=10009633" customname="所辖组织机构维护"><a href="javascript:void(0)">所辖组织机构维护</a></li><li customid="10009635" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/workflow_manager&amp;menuid=10009635" customname="工作流管理"><a href="javascript:void(0)">工作流管理</a></li><li customid="10010502" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/organizational_department&amp;menuid=10010502" customname="组织机构维护(部门)"><a href="javascript:void(0)">组织机构维护(部门)</a></li></ul></li><li class="" customid="10009608" opentype="0" customurl="" customname="数据源管理"><a href="javascript:void(0)">数据源管理<i></i></a><ul class="threeLevel"><li customid="10009610" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/physics_database_manager&amp;menuid=10009610" customname="物理数据库管理"><a href="javascript:void(0)">物理数据库管理</a></li></ul></li><li class="" customid="10009602" opentype="0" customurl="" customname="数据库和服务注册"><a href="javascript:void(0)">数据库和服务注册<i></i></a><ul class="threeLevel"><li customid="10009603" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/logicDataBase_manager&amp;menuid=10009603" customname="逻辑数据库管理"><a href="javascript:void(0)">逻辑数据库管理</a></li><li customid="10009604" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/micro_service&amp;menuid=10009604" customname="微服务注册"><a href="javascript:void(0)">微服务注册</a></li><li customid="10009605" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/ui_service&amp;menuid=10009605" customname="UI服务注册"><a href="javascript:void(0)">UI服务注册</a></li><li customid="10009606" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/webFunction&amp;menuid=10009606" customname="开发功能管理"><a href="javascript:void(0)">开发功能管理</a></li><li customid="10009607" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/user_features&amp;menuid=10009607" customname="用户功能管理"><a href="javascript:void(0)">用户功能管理</a></li><li customid="21005302" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/fileCenter-manager&amp;menuid=21005302" customname="文件中心配置"><a href="javascript:void(0)">文件中心配置</a></li></ul></li><li class="" customid="10009636" opentype="0" customurl="" customname="基础数据和枚举值管理"><a href="javascript:void(0)">基础数据和枚举值管理<i></i></a><ul class="threeLevel"><li customid="10009638" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/element_manager&amp;menuid=10009638" customname="要素管理"><a href="javascript:void(0)">要素管理</a></li><li customid="10009637" opentype="0" customurl="" customname="即时基础数据同步"><a href="javascript:void(0)">即时基础数据同步</a></li><li customid="10009642" opentype="0" customurl="" customname="枚举值更新到缓存"><a href="javascript:void(0)">枚举值更新到缓存</a></li><li customid="10009640" opentype="0" customurl="" customname="基础数据变更发布"><a href="javascript:void(0)">基础数据变更发布</a></li><li customid="10009639" opentype="0" customurl="" customname="基础数据维护"><a href="javascript:void(0)">基础数据维护</a></li><li customid="10009641" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/enumerationManagement&amp;menuid=10009641" customname="枚举值管理"><a href="javascript:void(0)">枚举值管理</a></li><li customid="500053" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/element_enable&amp;menuid=500053" customname="核算要素启用"><a href="javascript:void(0)">核算要素启用</a></li></ul></li><li class="" customid="10009652" opentype="0" customurl="" customname="序列号管理及单号规则"><a href="javascript:void(0)">序列号管理及单号规则<i></i></a><ul class="threeLevel"><li customid="10009653" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/singleRuleMent&amp;menuid=10009653" customname="单号规则管理(实施)"><a href="javascript:void(0)">单号规则管理(实施)</a></li><li customid="10009654" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/sequence_manager&amp;menuid=10009654" customname="序列号管理"><a href="javascript:void(0)">序列号管理</a></li><li customid="11815002" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/singleRuleDefine&amp;menuid=11815002" customname="单号规则定义(开发)"><a href="javascript:void(0)">单号规则定义(开发)</a></li></ul></li><li class="" customid="10009643" opentype="0" customurl="" customname="数据权限"><a href="javascript:void(0)">数据权限<i></i></a><ul class="threeLevel"><li customid="10009644" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/rightModel_manager&amp;menuid=10009644" customname="权限模型管理"><a href="javascript:void(0)">权限模型管理</a></li><li customid="10009645" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/right_manager&amp;menuid=10009645" customname="权限组管理"><a href="javascript:void(0)">权限组管理</a></li><li customid="10009646" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/elementValue_manager&amp;menuid=10009646" customname="定值规则"><a href="javascript:void(0)">定值规则</a></li><li customid="500060" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/eleRelation_manager&amp;menuid=500060" customname="要素关联关系"><a href="javascript:void(0)">要素关联关系</a></li></ul></li><li class="" customid="10009648" opentype="0" customurl="" customname="工作流管理及监控"><a href="javascript:void(0)">工作流管理及监控<i></i></a><ul class="threeLevel"><li customid="10009649" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/workday&amp;menuid=10009649" customname="工作日维护"><a href="javascript:void(0)">工作日维护</a></li><li customid="10009651" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/workflowMonitoring&amp;menuid=10009651" customname="工作流监控"><a href="javascript:void(0)">工作流监控</a></li></ul></li><li class="" customid="10009659" opentype="0" customurl="" customname="定时任务管理"><a href="javascript:void(0)">定时任务管理<i></i></a><ul class="threeLevel"><li customid="10009660" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/autoTask_manager&amp;menuid=10009660" customname="定时任务注册"><a href="javascript:void(0)">定时任务注册</a></li><li customid="10009661" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/autoSchedule_manager&amp;menuid=10009661" customname="定时任务调度设置"><a href="javascript:void(0)">定时任务调度设置</a></li></ul></li><li class="" customid="10009656" opentype="0" customurl="" customname="参数管理"><a href="javascript:void(0)">参数管理<i></i></a><ul class="threeLevel"><li customid="10009657" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/sysparameter_define&amp;menuid=10009657" customname="参数定义(开发)"><a href="javascript:void(0)">参数定义(开发)</a></li><li customid="10009658" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/sysparameter_manager&amp;menuid=10009658" customname="参数管理(实施)"><a href="javascript:void(0)">参数管理(实施)</a></li></ul></li><li class="" customid="10009669" opentype="0" customurl="" customname="第三方功能导入"><a href="javascript:void(0)">第三方功能导入<i></i></a><ul class="threeLevel"><li customid="10009670" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/third_uiService&amp;menuid=10009670" customname="第三方UI服务注册"><a href="javascript:void(0)">第三方UI服务注册</a></li><li customid="10009671" opentype="0" customurl="/framework-web/ctjview?path=grp/pt/common/html/three_manage&amp;menuid=10009671" customname="外部功能管理导入"><a href="javascript:void(0)">外部功能管理导入</a></li></ul></li></ul></div></div>
<!-- Top导航tabs -->
<div class="tabs1" style="left: 252px;">
<ul id="menu-tabs">
<li menu="1" class="focus1">
<a href="#">首页</a>
</li>
</ul>
<ul id="more-menu">
<li>
<span>更多</span>
<ul id="more-menu1" style="position: relative; max-height: 787px;">
<iframe frameborder="0" allowtransparency="true" scrolling="no" style="background-color:transparent; position: absolute; z-index: -1; width: 100%; height: 100%; top: 0;left:0;"></iframe>
</ul>
</li>
</ul>
</div>
<!-- index页面 -->
<div id="ifr1">
<iframe menu="1" class="show" src="/userportal-web/ctjview?path=grp/pt/common/html/index" frameborder="0"></iframe>
<div id="cover1"></div>
</div>

<script type="text/javascript" src="static/easyui/jquery.min.js"></script>
<script type="text/javascript" src="/framework-web/static/easyui/jquery.easyui.min.js"></script>
<script type="text/javascript" src="/framework-web/static/easyui/locale/easyui-lang-zh_CN.js"></script>
<script type="text/javascript" src="static/bootstrap/js/bootstrap.min.js"></script>
<script type="text/javascript" src="/framework-web/grp/pt/main/js/jquery.cookie.js"></script>
<script type="text/javascript" src="/framework-web/grp/pt/main/js/jquery.gridster.js"></script>
<script type="text/javascript" src="/framework-web/grp/pt/common/js/jquery.i18n.properties-min.js"></script>
<script language="javascript" src="/framework-web/grp/pt/main/js/mainHunan.js"></script>

</body></html>''')
