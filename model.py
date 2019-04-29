#!/usr/bin/env python3
#
# 2018年 11月 10日 星期六 07:16:38 CST

from gtk3_header import g, Vte
from widgets import FileEntry, NumberEntry

HORIZONTAL = g.Orientation.HORIZONTAL
cb = g.CheckButton.new_with_label
et = g.Entry


class Model(object):

  def __init__(self):
    # 目标url - burp日志 - HTTP请求...
    self._url_combobox = g.ComboBox.new_with_entry()
    self._burp_logfile = FileEntry()
    self._request_file = FileEntry()
    self._bulkfile = FileEntry()
    self._configfile = FileEntry()
    self._sitemap_url = g.Entry()
    self._google_dork = g.Entry()
  # 选项区(1)
  # sqlmap命令语句:
    self._cmd_entry = et()
  # 测试(Q)
    # 注入选项
    self._inject_area_param_ckbtn = cb('可测试的参数')
    self._inject_area_param_entry = et()
    self._inject_area_skip_static_ckbtn = cb('跳过无动态特性的参数')
    self._inject_area_prefix_ckbtn = cb('payload前缀')
    self._inject_area_prefix_entry = et()
    self._inject_area_suffix_ckbtn = cb('payload后缀')
    self._inject_area_suffix_entry = et()
    self._inject_area_skip_ckbtn = cb('排除参数')
    self._inject_area_skip_entry = et()
    self._inject_area_param_exclude_ckbtn = cb('排除参数(正则)')
    self._inject_area_param_exclude_entry = et()
    self._inject_area_dbms_ckbtn = cb('固定DB类型为')
    self._inject_area_dbms_combobox = g.ComboBox.new_with_entry()
    self._inject_area_dbms_cred_ckbtn = cb('DB认证')
    self._inject_area_dbms_cred_entry = et()
    self._inject_area_os_ckbtn = cb('固定OS为')
    self._inject_area_os_entry = et()
    self._inject_area_no_cast_ckbtn = cb('关掉payload变形机制')
    self._inject_area_no_escape_ckbtn = cb('关掉string转义')
    self._inject_area_invalid_logic_ckbtn = cb('使用逻辑运算符')
    self._inject_area_invalid_bignum_ckbtn = cb('使用大数')
    self._inject_area_invalid_str_ckbtn = cb('使用随机字符串')
    # 探测选项
    self._detection_area_level_ckbtn = cb('探测等级(范围)')
    self._detection_area_level_scale = g.Scale.new_with_range(HORIZONTAL, 1, 5, 1)
    self._detection_area_risk_ckbtn = cb('payload危险等级')
    self._detection_area_risk_scale = g.Scale.new_with_range(HORIZONTAL, 1, 3, 1)
    self._detection_area_str_ckbtn = cb('指定字符串')
    self._detection_area_str_entry = et()
    self._detection_area_not_str_ckbtn = cb('指定字符串')
    self._detection_area_not_str_entry = et()
    self._detection_area_re_ckbtn = cb('指定正则')
    self._detection_area_re_entry = et()
    self._detection_area_code_ckbtn = cb('指定http状态码')
    self._detection_area_code_entry = NumberEntry()
    self._detection_area_text_only_ckbtn = cb('仅对比文本')
    self._detection_area_titles_ckbtn = cb('仅对比title')
    # 各注入技术的选项
    self._tech_area_tech_ckbtn = cb('注入技术')
    self._tech_area_tech_entry = et()
    self._tech_area_time_sec_ckbtn = cb('指定DB延迟多少秒响应')
    self._tech_area_time_sec_entry = NumberEntry()
    self._tech_area_union_col_ckbtn = cb('指定最大union列数')
    self._tech_area_union_col_entry = NumberEntry()
    self._tech_area_union_chr_ckbtn = cb('指定枚举列数时所用字符')
    self._tech_area_union_chr_entry = et()
    self._tech_area_union_from_ckbtn = cb('指定枚举列数时from的表名')
    self._tech_area_union_from_entry = et()
    self._tech_area_dns_ckbtn = cb('指定DNS')
    self._tech_area_dns_entry = et()
    self._tech_area_second_url_ckbtn = cb('指定二阶响应的url')
    self._tech_area_second_url_entry = et()
    self._tech_area_second_req_ckbtn = cb('使用含二阶HTTP请求的文件:')
    self._tech_area_second_req_entry = FileEntry()
    # 性能优化
    self._optimize_area_turn_all_ckbtn = cb('启用所有优化选项')
    self._optimize_area_thread_num_ckbtn = cb('使用线程数:')
    self._optimize_area_thread_num_spinbtn = g.SpinButton.new_with_range(2, 1000, 2)
    self._optimize_area_predict_ckbtn = cb('预测通常的查询结果')
    self._optimize_area_keep_alive_ckbtn = cb('http连接使用keep-alive')
    self._optimize_area_null_connect_ckbtn = cb('只用页面长度报头来比较, 不去获取实际的响应体')
    # 常用选项
    self._general_area_verbose_ckbtn = cb('输出详细程度')
    self._general_area_verbose_scale = g.Scale.new_with_range(HORIZONTAL, 0, 6, 1)
    self._general_area_finger_ckbtn = cb('执行宽泛的DB版本检测')
    self._general_area_hex_ckbtn = cb('获取数据时使用hex转换')
    self._general_area_batch_ckbtn = cb('非交互模式, 一切皆默认')
    self._page1_misc_wizard_ckbtn = cb('新手向导')
  # 请求(W)
    # HTTP header
    self._request_area_random_agent_ckbtn = cb('随机User-Agent头')
    self._request_area_user_agent_ckbtn = cb('指定User-Agent头')
    self._request_area_user_agent_entry = et()
    self._request_area_host_ckbtn = cb('Host头')
    self._request_area_host_entry = et()
    self._request_area_referer_ckbtn = cb('referer头')
    self._request_area_referer_entry = et()
    self._request_area_header_ckbtn = cb('额外的header(-H)')
    self._request_area_header_entry = et()
    self._request_area_headers_ckbtn = cb('额外的headers')
    self._request_area_headers_entry = et()
    # HTTP data
    self._request_area_method_ckbtn = cb('HTTP请求方式')
    self._request_area_method_entry = et()
    self._request_area_param_del_ckbtn = cb('指定分隔data参数值的字符')
    self._request_area_param_del_entry = et()
    self._request_area_post_ckbtn = cb('通过POST提交data:')
    self._request_area_post_entry = et()
    self._request_area_cookie_ckbtn = cb('请求中要包含的Cookie:')
    self._request_area_cookie_entry = et()
    self._request_area_cookie_del_ckbtn = cb('指定cookie分隔符')
    self._request_area_cookie_del_entry = et()
    self._request_area_load_cookies_ckbtn = cb('本地Cookie文件')
    self._request_area_load_cookies_entry = FileEntry()
    self._request_area_drop_set_cookie_ckbtn = cb('丢弃Set-Cookie头')
    self._request_area_auth_type_ckbtn = cb('http认证类型')
    self._request_area_auth_type_entry = et()
    self._request_area_auth_cred_ckbtn = cb('http认证账密')
    self._request_area_auth_cred_entry = et()
    self._request_area_auth_file_ckbtn = cb('http认证文件')
    self._request_area_auth_file_entry = FileEntry()
    self._request_area_csrf_token_ckbtn = cb('csrf_token')
    self._request_area_csrf_token_entry = et()
    self._request_area_csrf_url_ckbtn = cb('获取csrf_token的url')
    self._request_area_csrf_url_entry = et()
    # request定制
    self._request_area_ignore_redirects_ckbtn = cb('忽略重定向')
    self._request_area_ignore_timeouts_ckbtn = cb('忽略连接超时')
    self._request_area_ignore_code_ckbtn = cb('忽略错误型状态码:')
    self._request_area_ignore_code_entry = NumberEntry()
    self._request_area_skip_urlencode_ckbtn = cb('payload不使用url编码')
    self._request_area_force_ssl_ckbtn = cb('强制使用HTTPS')
    self._request_area_chunked_ckbtn = cb('用Chunked编码发送POST请求')
    self._request_area_hpp_ckbtn = cb('使用HTTP参数污染')
    self._request_area_delay_ckbtn = cb('请求间隔(秒)')
    self._request_area_delay_entry = NumberEntry()
    self._request_area_timeout_ckbtn = cb('几秒超时')
    self._request_area_timeout_entry = NumberEntry()
    self._request_area_retries_ckbtn = cb('超时重试次数')
    self._request_area_retries_entry = NumberEntry()
    self._request_area_randomize_ckbtn = cb('指定要随机改变值的参数')
    self._request_area_randomize_entry = et()
    self._request_area_eval_ckbtn = cb('--eval=')
    self._request_area_eval_entry = et()
    # 隐匿/代理
    self._request_area_safe_url_ckbtn = cb('顺便掺杂地访问一个安全url')
    self._request_area_safe_url_entry = et()
    self._request_area_safe_post_ckbtn = cb('提交到安全url的post数据')
    self._request_area_safe_post_entry = et()
    self._request_area_safe_req_ckbtn = cb('从文件载入safe HTTP请求')
    self._request_area_safe_req_entry = FileEntry()
    self._request_area_safe_freq_ckbtn = cb('访问安全url的频率')
    self._request_area_safe_freq_entry = et()
    self._request_area_ignore_proxy_ckbtn = cb('忽略系统默认代理')
    self._request_area_proxy_ckbtn = cb('使用代理')
    self._request_area_proxy_file_ckbtn = cb('代理列表文件')
    self._request_area_proxy_file_entry = FileEntry()
    self._request_area_proxy_ip_label = g.Label.new('IP:')
    self._request_area_proxy_ip_entry = et()
    self._request_area_proxy_port_label = g.Label.new('PORT:')
    self._request_area_proxy_port_entry = NumberEntry()
    self._request_area_proxy_username_label = g.Label.new('username:')
    self._request_area_proxy_username_entry = et()
    self._request_area_proxy_password_label = g.Label.new('password:')
    self._request_area_proxy_password_entry = et()
    self._request_area_tor_ckbtn = cb('使用Tor匿名网络')
    self._request_area_tor_port_ckbtn = cb('Tor端口')
    self._request_area_tor_port_entry = NumberEntry()
    self._request_area_tor_type_ckbtn = cb('Tor代理类型')
    self._request_area_tor_type_entry = et()
    self._request_area_check_tor_ckbtn = cb('检查Tor连接')
  # 枚举(E)
    # 枚举
    self._enum_area_opts_ckbtns = (
      (cb('DB banner'), cb('当前用户'), cb('当前数据库'), cb('主机名'), cb('是否是DBA')),
      (cb('用户'), cb('密码'), cb('权限'), cb('角色'), cb('数据库')),
      (cb('表'), cb('字段'), cb('架构'), cb('计数'), cb('备注')),
    )
    # Dump(转储)
    self._dump_area_dump_ckbtn = cb('dump(某库某表的条目)')
    self._dump_area_dump_all_ckbtn = cb('全部dump(拖库)')
    self._dump_area_search_ckbtn = cb('搜索')
    self._dump_area_no_sys_db_ckbtn = cb('排除系统库')
    self._dump_area_repair_ckbtn = cb('重新获取有未知符号(?)的条目')
    # limit(dump时的限制)
    self._limit_area_start_ckbtn = cb('始于第')
    self._limit_area_start_entry = NumberEntry()
    self._limit_area_stop_ckbtn = cb('止于第')
    self._limit_area_stop_entry = NumberEntry()
    # 盲注选项
    self._blind_area_first_ckbtn = cb('首字符')
    self._blind_area_first_entry = et()
    self._blind_area_last_ckbtn = cb('末字符')
    self._blind_area_last_entry = et()
    # 数据库名, 表名, 列名...
    self._meta_area_D_ckbtn = cb('指定库名')
    self._meta_area_D_entry = et()
    self._meta_area_T_ckbtn = cb('指定表名')
    self._meta_area_T_entry = et()
    self._meta_area_C_ckbtn = cb('指定列名')
    self._meta_area_C_entry = et()
    self._meta_area_U_ckbtn = cb('指定用户')
    self._meta_area_U_entry = et()
    self._meta_area_X_ckbtn = cb('排除标志符')
    self._meta_area_X_entry = et()
    self._meta_area_pivot_ckbtn = cb('指定Pivot列名')
    self._meta_area_pivot_entry = et()
    self._meta_area_where_ckbtn = cb('where子句')
    self._meta_area_where_entry = et()
    # 执行SQL语句
    self._runsql_area_sql_query_ckbtn = cb('SQL语句:')
    self._runsql_area_sql_query_entry = et()
    self._runsql_area_sql_shell_ckbtn = cb('打开个SQL交互shell')
    self._runsql_area_sql_file_ckbtn = cb('本地SQL文件:')
    self._runsql_area_sql_file_entry = FileEntry()
    # 暴破表名/列名
    self._brute_force_area_common_tables_ckbtn = cb('常用表名')
    self._brute_force_area_common_columns_ckbtn = cb('常用列名')
  # 文件(R)
    # 读取远程文件
    self._file_read_area_file_read_ckbtn = cb('远程文件路径(--file-read=)')
    self._file_read_area_file_read_entry = et()
    self._file_read_area_file_btn = g.Button.new_with_label('查看')
    # 文件上传
    self._file_write_area_udf_ckbtn = cb('注入(默认sqlmap自带的)用户定义函数')
    self._file_write_area_shared_lib_ckbtn = cb('本地共享库路径(--shared-lib=)')
    self._file_write_area_shared_lib_entry = FileEntry()
    self._file_write_area_file_write_ckbtn = cb('本地文件路径(--file-write=)')
    self._file_write_area_file_write_entry = FileEntry()
    self._file_write_area_file_dest_ckbtn = cb('远程文件路径(--file-dest=)')
    self._file_write_area_file_dest_entry = et()
    # 访问后端OS
    self._file_os_access_os_cmd_ckbtn = cb('执行CLI命令')
    self._file_os_access_os_cmd_entry = et()
    self._file_os_access_os_shell_ckbtn = cb('获取交互shell')
    self._file_os_access_os_pwn_ckbtn = cb('--os-pwn')
    self._file_os_access_os_smbrelay_ckbtn = cb('--os-smbrelay')
    self._file_os_access_os_bof_ckbtn = cb('--os-bof')
    self._file_os_access_priv_esc_ckbtn = cb('--priv-esc')
    self._file_os_access_msf_path_ckbtn = cb('本地Metasploit安装路径')
    self._file_os_access_msf_path_entry = FileEntry()
    self._file_os_access_tmp_path_ckbtn = cb('远程临时目录(绝对路径)')
    self._file_os_access_tmp_path_entry = et()
    # 访问WIN下注册表
    self._file_os_registry_reg_ckbtn = cb('键值操作:')
    self._file_os_registry_reg_combobox = g.ComboBoxText.new()
    self._file_os_registry_reg_key_label = g.Label.new('键')
    self._file_os_registry_reg_key_entry = et()
    self._file_os_registry_reg_value_label = g.Label.new('值')
    self._file_os_registry_reg_value_entry = et()
    self._file_os_registry_reg_data_label = g.Label.new('数据')
    self._file_os_registry_reg_data_entry = et()
    self._file_os_registry_reg_type_label = g.Label.new('类型')
    self._file_os_registry_reg_type_entry = et()
  # 其他(T)
    # 通用项
    self._page1_general_check_internet_ckbtn = cb('检查与目标的网络连接')
    self._page1_general_fresh_queries_ckbtn = cb('刷新此次查询')
    self._page1_general_flush_session_ckbtn = cb('清空目标的会话文件')
    self._page1_general_eta_ckbtn = cb('显示剩余时间')
    self._page1_general_binary_fields_ckbtn = cb('生成有二进制值的字段')
    self._page1_general_binary_fields_entry = et()
    self._page1_general_forms_ckbtn = cb('解析和测试目标url内的表单')
    self._page1_general_parse_errors_ckbtn = cb('解析并显示DB错误信息')
    self._page1_misc_cleanup_ckbtn = cb('清理DBMS中sqlmap产生的UDF和表')
    self._page1_general_preprocess_ckbtn = cb('指定预处理响应数据的脚本')
    self._page1_general_preprocess_entry = et()
    self._page1_general_crawl_ckbtn = cb('爬网站(的层级/深度)')
    self._page1_general_crawl_entry = NumberEntry()
    self._page1_general_crawl_exclude_ckbtn = cb('爬站时排除(正则)页面')
    self._page1_general_crawl_exclude_entry = et()
    self._page1_general_charset_ckbtn = cb('盲注所用的字符集合')
    self._page1_general_charset_entry = et()
    self._page1_general_encoding_ckbtn = cb('字符编码(用于数据获取)')
    self._page1_general_encoding_entry = et()
    self._page1_general_session_file_ckbtn = cb('指定会话文件')
    self._page1_general_session_file_entry = FileEntry()
    self._page1_general_output_dir_ckbtn = cb('输出的保存目录')
    self._page1_general_output_dir_entry = FileEntry()
    self._page1_general_dump_format_ckbtn = cb('dump结果的文件格式')
    self._page1_general_dump_format_entry = et()
    self._page1_general_csv_del_ckbtn = cb('(csv文件的)分隔符')
    self._page1_general_csv_del_entry = et()
    self._page1_general_traffic_file_ckbtn = cb('转存所有http流量到文本')
    self._page1_general_traffic_file_entry = FileEntry()
    self._page1_general_har_ckbtn = cb('转存至HAR文件')
    self._page1_general_har_entry = FileEntry()
    self._page1_general_save_ckbtn = cb('保存选项至INI文件')
    self._page1_general_save_entry = FileEntry()
    self._page1_general_scope_ckbtn = cb('从代理日志过滤出目标(正则)')
    self._page1_general_scope_entry = FileEntry()
    self._page1_general_test_filter_ckbtn = cb('测试过滤器(从payload/title选择)')
    self._page1_general_test_filter_entry = et()
    self._page1_general_test_skip_ckbtn = cb('测试跳过(从payload/title选择)')
    self._page1_general_test_skip_entry = et()
    # 杂项
    self._page1_misc_web_root_ckbtn = cb('远程web的root目录')
    self._page1_misc_web_root_entry = et()
    self._page1_misc_tmp_dir_ckbtn = cb('本地临时目录')
    self._page1_misc_tmp_dir_entry = FileEntry()
    self._page1_misc_identify_waf_ckbtn = cb('鉴别WAF')
    self._page1_misc_skip_waf_ckbtn = cb('跳过对WAF/IPS保护的启发式侦测')
    self._page1_misc_smart_ckbtn = cb('只对明显注入点进行详细测试')
    self._page1_misc_list_tampers_ckbtn = cb('列出可用的tamper脚本')
    self._page1_misc_sqlmap_shell_ckbtn = cb('打开sqlmap交互shell')
    self._page1_misc_disable_color_ckbtn = cb('禁用终端输出的颜色')
    self._page1_misc_offline_ckbtn = cb('离线模式(只使用保存的会话数据)')
    self._page1_misc_mobile_ckbtn = cb('模拟手机请求')
    self._page1_misc_beep_ckbtn = cb('响铃')
    self._page1_misc_purge_ckbtn = cb('彻底清除所有记录')
    self._page1_misc_dependencies_ckbtn = cb('检查丢失的(非核心的)sqlmap依赖')
    self._page1_general_update_ckbtn = cb('更新sqlmap')
    self._page1_misc_answers_ckbtn = cb('设置交互时的问题答案:')
    self._page1_misc_answers_entry = et()
    self._page1_misc_alert_ckbtn = cb('发现注入时运行本地命令:')
    self._page1_misc_alert_entry = et()
    self._page1_misc_gpage_ckbtn = cb('GOOGLEDORK时的页码')
    self._page1_misc_gpage_spinbtn = g.SpinButton.new_with_range(1, 100, 1)
    self._page1_misc_z_ckbtn = cb('使用短的助记符')
    self._page1_misc_z_entry = et()
  # 输出区(2)
    # self._page2_cmdline_str_label = g.Label.new('')
    self._page2_respwan_btn = g.Button.new_with_label('重开终端')
    self._page2_terminal = Vte.Terminal.new()
  # 日志区(3)
    self._page3_clear_btn = g.Button.new_with_mnemonic('清空(_C)')
  # API区(4)
    self._page4_api_server_label = g.Label.new('REST-JSON API server:')
    self._page4_api_server_entry = et()
    self._page4_admin_token_label = g.Label.new('Admin (secret) token:')
    self._page4_admin_token_entry = et()
    self._page4_task_new_btn = g.Button.new_with_label('创建任务')
    self._page4_admin_list_btn = g.Button.new_with_label('显示任务')
    self._page4_admin_flush_btn = g.Button.new_with_label('删除所有任务')
    self._page4_clear_task_view_btn = g.Button.new_with_label('清空反馈的结果')
    self._page4_option_get_entry = et()
    self._page4_option_set_view = g.TextView()
    self._page4_task_view = g.TextView()


def main():
  pass


if __name__ == '__main__':
  main()
