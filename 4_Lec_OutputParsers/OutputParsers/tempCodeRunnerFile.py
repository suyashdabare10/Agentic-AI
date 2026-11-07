prompt = template.invoke({'place':'Indian'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)