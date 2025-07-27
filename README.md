# 🔗 VIRA MCP Server

**A clean, focused Model Context Protocol server that provides AI agent capabilities through standardized MCP workflows.**

This MCP server acts as a bridge between MCP clients (like Claude Desktop, Claude Code, Cursor) and VIRA's intelligent agent system, exposing agent capabilities through workflow-based tools built on the modern `mcp_agent` framework.

## 🎯 What This Server Provides

**Modern MCP Workflow Implementation**
- Workflow-based agent definitions
- Automatic MCP tool generation
- Parallel agent execution capabilities
- Built-in LLM integration and management

**Agent Integration Layer**
- Coordinates with specialized AI workflows
- Routes requests to appropriate agent capabilities
- Manages multi-agent collaboration
- Provides unified responses to MCP clients

## 🛠️ Available MCP Workflows

### Core Agent Workflows

**`PlanningWorkflow`**
```json
{
  "task_description": "Create a Python web scraper for news articles with error handling and data validation"
}
```
*Autonomous task planning, decomposition, and execution coordination*

**`ResearchWorkflow`**
```json
{
  "research_topic": "Best practices for Python web scraping in 2024"
}
```
*Comprehensive research, analysis, and actionable insights generation*

**`CodeDevelopmentWorkflow`**
```json
{
  "dev_request": {
    "task": "Build a REST API for user management",
    "language": "python",
    "requirements": "FastAPI, JWT auth, PostgreSQL integration"
  }
}
```
*End-to-end software development with parallel specialist agents (Architect, Developer, Tester, Reviewer)*

**`VIRAOrchestrationWorkflow`**
```json
{
  "project_request": {
    "description": "Build and deploy a complete e-commerce platform",
    "type": "full_stack_development",
    "priority": "high"
  }
}
```
*Master coordination of multiple agents for complex, multi-phase projects*

**`ClaudeCodeIntegrationWorkflow`**
```json
{
  "code_request": {
    "operation": "refactor",
    "target": "/path/to/project",
    "prompt": "Optimize performance and add comprehensive error handling"
  }
}
```
*Repository management, code analysis, and Claude Code CLI integration*

## 📋 Installation & Setup

### 1. Basic Installation

```bash
# Clone repository
git clone <repository-url>
cd vira-mcp-server

# Install dependencies (including mcp_agent framework)
pip install -r requirements.txt

# Set up API keys
export ANTHROPIC_API_KEY="your-anthropic-key"
export OPENAI_API_KEY="your-openai-key"  # Optional

# Make executable
chmod +x vira_mcp_server.py
```

### 2. MCP Client Configuration

**Claude Desktop** (`~/Library/Application Support/Claude/claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "vira-agents": {
      "command": "python3",
      "args": ["/absolute/path/to/vira-mcp-server/vira_mcp_server.py"],
      "env": {
        "PYTHONPATH": "/absolute/path/to/vira-mcp-server",
        "ANTHROPIC_API_KEY": "your-key-here",
        "OPENAI_API_KEY": "your-key-here"
      }
    }
  }
}
```

**Claude Code** (Project-scoped):
```bash
# Use the included .mcp.json file
cd vira-mcp-server
claude mcp list
```

**Claude Code** (User-scoped):
```bash
claude mcp add vira-agents -s user \
  -e ANTHROPIC_API_KEY=your-key \
  -e OPENAI_API_KEY=your-key \
  -- python3 /absolute/path/to/vira_mcp_server.py
```

**Cursor** (`~/.cursor/mcp.json`):
```json
{
  "mcpServers": {
    "vira-agents": {
      "command": "python3",
      "args": ["/absolute/path/to/vira-mcp-server/vira_mcp_server.py"],
      "env": {
        "ANTHROPIC_API_KEY": "your-key-here",
        "OPENAI_API_KEY": "your-key-here"
      }
    }
  }
}
```

### 3. Verification

```bash
# Test server directly
python3 vira_mcp_server.py

# Expected output:
# 🤖 VIRA Agent System Initializing...
# 🎯 Specialized Agent Workflows Available:
#   🔧 PlanningWorkflow: Task planning and execution coordination
#   🔧 ResearchWorkflow: Autonomous research and analysis
#   🔧 CodeDevelopmentWorkflow: End-to-end software development
#   🔧 VIRAOrchestrationWorkflow: Multi-agent project coordination
#   🔧 ClaudeCodeIntegrationWorkflow: Repository management
# ✅ VIRA Agent System Ready - All specialized agents online!
```

## 🔧 Server Architecture

```
MCP Agent Server (mcp_agent framework)
├── Workflow Layer
│   ├── PlanningWorkflow → Planning Agent
│   ├── ResearchWorkflow → Research Agent  
│   ├── CodeDevelopmentWorkflow → Parallel Dev Agents
│   ├── VIRAOrchestrationWorkflow → Master Coordinator
│   └── ClaudeCodeIntegrationWorkflow → Claude CLI
├── Agent Execution Layer
│   ├── Parallel LLM Execution
│   ├── Context Management
│   └── Tool Integration
└── MCP Protocol Layer
    ├── Automatic Tool Generation
    ├── Request/Response Handling
    └── Client Communication
```

## 📊 MCP Protocol Compliance

**Framework Benefits:**
- ✅ Automatic MCP tool generation from workflows
- ✅ Built-in parallel agent execution
- ✅ Context preservation across interactions
- ✅ Intelligent LLM selection and management
- ✅ Type-safe workflow definitions

**Transport Methods:**
- ✅ STDIO (primary)
- ✅ HTTP (framework managed)
- ✅ WebSocket (framework managed)

**Security Features:**
- ✅ Environment-based API key management
- ✅ Sandboxed workflow execution
- ✅ Input validation and sanitization
- ✅ Resource usage monitoring
- ✅ Timeout enforcement

## 🚀 Usage Examples

### Autonomous Project Planning

```bash
# Through MCP client
"Plan the development of a complete FastAPI application with React frontend"

# PlanningWorkflow will:
# 1. Analyze project requirements
# 2. Break down into phases (backend, frontend, integration)
# 3. Create detailed execution steps
# 4. Estimate timelines and resources
# 5. Identify potential risks and dependencies
```

### Multi-Agent Code Development

```bash
# Through MCP client
"Build a user authentication system with JWT tokens and password reset functionality"

# CodeDevelopmentWorkflow will coordinate:
# - Architect Agent: Design system architecture
# - Developer Agent: Implement clean, documented code
# - Tester Agent: Create comprehensive test suites
# - Reviewer Agent: Conduct security and quality review
```

### Comprehensive Research

```bash
# Through MCP client
"Research the latest AI agent frameworks and recommend the best approach for building autonomous systems"

# ResearchWorkflow will:
# 1. Investigate current frameworks and technologies
# 2. Analyze strengths, weaknesses, and use cases
# 3. Compare performance and capabilities
# 4. Generate actionable recommendations
# 5. Provide implementation guidance
```

### Master Project Orchestration

```bash
# Through MCP client
"Build and deploy a complete e-commerce platform with payment processing, inventory management, and admin dashboard"

# VIRAOrchestrationWorkflow will:
# 1. Coordinate multiple specialized workflows
# 2. Manage dependencies between components
# 3. Orchestrate frontend and backend development
# 4. Handle deployment and testing strategies
# 5. Integrate all system components
```

## 🔍 Monitoring & Debugging

### Workflow Status

```bash
# Check active workflows through MCP client
"Show me the status of all active workflows and agents"

# Returns real-time status of:
# - Currently executing workflows
# - Agent performance metrics
# - Resource utilization
# - Completion statistics
```

### Debug Mode

```bash
# Enable debug logging
export LOG_LEVEL=DEBUG
export ANTHROPIC_API_KEY=your-key
python3 vira_mcp_server.py
```

### Performance Metrics

The framework automatically tracks:
- Workflow execution times
- Agent collaboration efficiency
- LLM token usage and costs
- Success/failure rates
- Resource optimization metrics

## ⚙️ Configuration

### Environment Variables

```bash
# Required
ANTHROPIC_API_KEY=your-anthropic-key

# Optional
OPENAI_API_KEY=your-openai-key
LOG_LEVEL=INFO                    # DEBUG, INFO, WARNING, ERROR
PYTHONPATH=.                      # Ensure proper module imports
```

### Advanced Workflow Configuration

Each workflow can be fine-tuned with model preferences:

```python
# Example: High intelligence, low cost priority
RequestParams(
    modelPreferences=ModelPreferences(
        intelligencePriority=0.9,
        costPriority=0.05,
        speedPriority=0.05,
    )
)
```

## 🛡️ Security

### API Key Management
- Environment variable-based configuration
- No hardcoded secrets in code
- Secure credential handling by framework

### Workflow Isolation
- Sandboxed agent execution
- Resource usage limits
- Timeout enforcement for all operations
- Safe parallel execution management

### Data Protection
- No sensitive data in logs
- Secure inter-agent communication
- Context isolation between workflows
- Automatic cleanup after execution

## 🔧 Extending the Server

### Adding New Workflows

```python
@app.workflow
class CustomWorkflow(Workflow[str]):
    """Custom workflow for specialized tasks"""

    @app.workflow_run
    async def run(self, input: str) -> WorkflowResult[str]:
        custom_agent = Agent(
            name="custom_specialist",
            instruction="Your specialized instructions...",
            server_names=["filesystem", "fetch"] if available else [],
        )
        
        async with custom_agent:
            llm = await custom_agent.attach_llm(AnthropicAugmentedLLM)
            result = await llm.generate_str(message=input)
            return WorkflowResult(value=result)
```

### Customizing Agent Behavior

```python
# Modify agent instructions for specific workflows
Agent(
    name="domain_expert",
    instruction="""You are a specialist in [domain]. Your expertise includes:
    1. [Specific capability 1]
    2. [Specific capability 2] 
    3. [Specific capability 3]
    
    Always [behavioral guidelines].""",
    server_names=["relevant", "servers"],
)
```

## 📈 Performance

**Framework-Optimized Performance:**
- Workflow initialization: < 500ms
- Agent coordination: < 1s
- Parallel execution: Multiple agents simultaneously
- Research workflows: < 45s for comprehensive analysis
- Code development: < 2 minutes for complete solutions
- Project orchestration: Scales with project complexity

**Resource Efficiency:**
- Automatic LLM selection based on task complexity
- Intelligent token usage optimization
- Parallel processing for faster completion
- Context preservation to avoid redundant processing

## 🐛 Troubleshooting

### Common Issues

**"Workflow not found"**
- Verify workflow registration with `@app.workflow` decorator
- Check that workflow run method has `@app.workflow_run` decorator
- Ensure proper import of workflow classes

**"API key not configured"**
- Set environment variables: `ANTHROPIC_API_KEY` and optionally `OPENAI_API_KEY`
- Verify keys are exported in shell environment
- Check MCP client configuration includes API keys

**"Agent execution failing"**
- Enable debug logging: `export LOG_LEVEL=DEBUG`
- Check agent instruction clarity and specificity
- Verify server access (filesystem, fetch) if required
- Review workflow input parameters

### Debugging Steps

1. **Enable verbose logging**: `LOG_LEVEL=DEBUG`
2. **Test framework installation**: `python3 -c "import mcp_agent; print('OK')"`
3. **Verify API connectivity**: Test with simple workflow
4. **Check MCP client logs**: Review client-side messages
5. **Monitor resource usage**: Watch memory and token consumption

## 📚 Related Documentation

- [mcp_agent Framework Documentation](https://github.com/lastmile-ai/mcp-agent)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Anthropic MCP Guide](https://docs.anthropic.com/en/docs/build-with-claude/mcp)
- [Claude Code Integration](https://docs.anthropic.com/en/docs/claude-code/mcp)

---

**The VIRA MCP Server leverages the modern mcp_agent framework to provide clean, workflow-based access to powerful AI agent capabilities. The framework handles MCP protocol details automatically while enabling sophisticated multi-agent coordination and parallel execution.** 🤖✨
