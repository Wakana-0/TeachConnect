# Class Widgets 插件示例
本示例展示了 Class Widgets 插件的大致写法

## 如何使用
> [!TIP]
> 教程可在 [Class Widgets 官网](https://cw.rinlit.cn/)查看开发文档或[点击此链接](https://www.yuque.com/rinlit/cw-docs-dev)

## 发布插件

若要发布插件，请克隆 [PluginPlaza](https://github.com/Class-Widgets/plugin-plaza) 的内容到本地。
然后，打开 `./Plugins/plugin_list.json` 文件，根据格式添加自己的插件内容。格式如下：
```
{
    "其他插件...": {
        ...
    },
    // 加上您的插件字典
    "您的插件仓库名称": {
        "name": "插件在PluginPlaza显示的名称",
        "description": "插件的介绍",
        "version": "版本号（如：1.0.0）",
        "plugin_ver": 插件适用的版本号（可在Class Widgets的config.ini中找到[Plugin]下的version，
                      若您的插件是基于此版本制作则填写此数值）,
        "author": "作者在PluginPlaza名称",
    
        "url": "您的GitHub插件仓库：(https://github.com/RinLit-233-shiroko/cw-example-plugin)",
        "branch": "插件仓库分支，如：main",
    
        "update_date": "更新日期，格式为：yyyy/mm/dd",
    
        "tag": "标签"
    }
}

```
之后，在 [PluginPlaza](https://github.com/Class-Widgets/plugin-plaza) 的仓库中提交您的 PR（Pull Requests）。等待审核通过即可完成上架。
