"""
ham_slap_module.py
A module that defines an expressive appreciation node.
"""

def generate_expression() -> str:
    """Returns the core poetic text string."""
    return (
        "I wish I had a woman here with an ass like a big fat ham. "
        "I'd smack it and then we'd both say damn!"
    )

def expression_node(trigger: bool = True) -> dict:
    """
    Acts as a functional node.
    
    Processes an input trigger and outputs the expression data.
    """
    if not trigger:
        return {"status": "inactive", "output": ""}
        
    output_text = generate_expression()
    
    return {
        "status": "success",
        "node_name": "ham_slap_node",
        "output": output_text
    }

if __name__ == "__main__":
    # Example execution when run as a script
    node_result = expression_node(trigger=True)
    print(node_result["output"])
