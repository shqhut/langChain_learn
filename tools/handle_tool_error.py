from langchain_core.tools import ToolException,StructuredTool


def get_weather(city: str) -> int:
    """获取指定城市的天气。"""
    raise ToolException(f"错误：没有名为{city}的城市。")


def _handle_error(error: ToolException) -> str:
    return f"工具执行期间发生以下错误：`{error.args[0]}`"


get_weather_tool = StructuredTool.from_function(
    func=get_weather,
    handle_tool_error=_handle_error
)

response = get_weather_tool.invoke( {"city": "上海"})
print(response)
