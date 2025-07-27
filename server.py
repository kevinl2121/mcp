"""
VIRA Agent MCP Server - Simplified using mcp_agent framework

This demonstrates a clean agent-based MCP server with specialized AI agents
following the modern mcp_agent patterns.
"""

import asyncio
import os
import logging
from typing import Dict, Any

from mcp_agent.app import MCPApp
from mcp_agent.server.app_server import create_mcp_server_for_app
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm import RequestParams
from mcp_agent.workflows.llm.llm_selector import ModelPreferences
from mcp_agent.workflows.llm.augmented_llm_anthropic import AnthropicAugmentedLLM
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM
from mcp_agent.workflows.parallel.parallel_llm import ParallelLLM
from mcp_agent.executor.workflow import Workflow, WorkflowResult

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the VIRA app
app = MCPApp(
    name="vira_agent_server", 
    description="VIRA - Virtual Intelligent Recursive Agent system with specialized AI agents"
)


@app.workflow
class PlanningWorkflow(Workflow[str]):
    """
    Autonomous task planning and execution workflow.
    This agent breaks down complex tasks into manageable steps and coordinates execution.
    """

    @app.workflow_run
    async def run(self, task_description: str) -> WorkflowResult[str]:
        """
        Plan and execute a complex task autonomously.

        Args:
            task_description: Description of the task to plan and execute

        Returns:
            WorkflowResult containing the execution plan and results
        """
        
        logger.info(f"PlanningWorkflow received task: {task_description}")
        
        # Add current directory to filesystem access if available
        context = app.context
        if "filesystem" in context.config.mcp.servers:
            context.config.mcp.servers["filesystem"].args.extend([os.getcwd()])

        planning_agent = Agent(
            name="planning_agent",
            instruction="""You are VIRA's Planning Agent - an expert at breaking down complex tasks 
            into manageable, sequential steps. Your responsibilities:
            
            1. Analyze the task and understand requirements
            2. Break down into logical, executable steps
            3. Identify dependencies and prerequisites
            4. Estimate time and resources needed
            5. Create a detailed execution plan
            6. Monitor progress and adapt as needed
            
            Always provide structured, actionable plans with clear deliverables.""",
            server_names=["filesystem"] if "filesystem" in context.config.mcp.servers else [],
        )

        async with planning_agent:
            logger.info("Planning Agent: Connected, analyzing task...")
            
            llm = await planning_agent.attach_llm(AnthropicAugmentedLLM)
            
            # Generate initial plan
            plan_result = await llm.generate_str(
                message=f"""Analyze this task and create a detailed execution plan: {task_description}
                
                Please provide:
                1. Task analysis and requirements
                2. Step-by-step execution plan
                3. Resource requirements
                4. Time estimates
                5. Success criteria
                6. Potential risks and mitigation strategies
                
                Format as a structured plan that can be executed autonomously.""",
                request_params=RequestParams(
                    modelPreferences=ModelPreferences(
                        intelligencePriority=0.8,
                        costPriority=0.1,
                        speedPriority=0.1,
                    )
                )
            )
            
            logger.info(f"Planning completed: {len(plan_result)} characters generated")
            return WorkflowResult(value=plan_result)


@app.workflow
class ResearchWorkflow(Workflow[str]):
    """
    Autonomous research and analysis workflow.
    This agent conducts comprehensive research on topics and generates insights.
    """

    @app.workflow_run
    async def run(self, research_topic: str) -> WorkflowResult[str]:
        """
        Conduct autonomous research on a topic.

        Args:
            research_topic: The topic to research

        Returns:
            WorkflowResult containing comprehensive research findings
        """
        
        logger.info(f"ResearchWorkflow investigating: {research_topic}")
        
        context = app.context
        available_servers = ["fetch"] if "fetch" in context.config.mcp.servers else []
        
        research_agent = Agent(
            name="research_agent",
            instruction="""You are VIRA's Research Agent - an expert investigator and analyst.
            Your capabilities include:
            
            1. Comprehensive topic investigation
            2. Multi-source information gathering
            3. Critical analysis and synthesis
            4. Trend identification and pattern recognition
            5. Evidence-based conclusions
            6. Actionable insights generation
            
            Always provide thorough, well-sourced research with clear methodology and findings.""",
            server_names=available_servers,
        )

        async with research_agent:
            logger.info("Research Agent: Connected, beginning investigation...")
            
            llm = await research_agent.attach_llm(AnthropicAugmentedLLM)
            
            # Conduct research
            research_result = await llm.generate_str(
                message=f"""Conduct comprehensive research on: {research_topic}
                
                Please provide:
                1. Research methodology and approach
                2. Key findings and discoveries
                3. Analysis of current trends and developments
                4. Critical evaluation of sources and evidence
                5. Synthesized insights and conclusions
                6. Actionable recommendations
                7. Areas for further investigation
                
                Ensure the research is thorough, objective, and provides practical value.""",
                request_params=RequestParams(
                    modelPreferences=ModelPreferences(
                        intelligencePriority=0.9,
                        costPriority=0.05,
                        speedPriority=0.05,
                    )
                )
            )
            
            logger.info(f"Research completed: comprehensive analysis generated")
            return WorkflowResult(value=research_result)


@app.workflow
class CodeDevelopmentWorkflow(Workflow[Dict[str, str]]):
    """
    Autonomous code development workflow.
    This workflow handles end-to-end software development tasks.
    """

    @app.workflow_run
    async def run(self, dev_request: Dict[str, str]) -> WorkflowResult[str]:
        """
        Develop code based on requirements.

        Args:
            dev_request: Dictionary with 'task', 'language', and 'requirements'

        Returns:
            WorkflowResult containing the developed code and documentation
        """
        
        task = dev_request.get('task', 'Code development task')
        language = dev_request.get('language', 'python')
        requirements = dev_request.get('requirements', 'Standard best practices')
        
        logger.info(f"CodeDevelopmentWorkflow: {task} in {language}")
        
        context = app.context
        if "filesystem" in context.config.mcp.servers:
            context.config.mcp.servers["filesystem"].args.extend([os.getcwd()])

        # Create specialized development agents
        architect_agent = Agent(
            name="architect",
            instruction="""You are a Software Architect. Design system architecture, 
            define interfaces, and create technical specifications. Focus on scalability, 
            maintainability, and best practices.""",
            server_names=["filesystem"] if "filesystem" in context.config.mcp.servers else [],
        )

        developer_agent = Agent(
            name="developer", 
            instruction="""You are a Senior Developer. Write clean, efficient, well-documented code.
            Implement the architecture specifications with proper error handling, logging, 
            and following language-specific best practices.""",
            server_names=["filesystem"] if "filesystem" in context.config.mcp.servers else [],
        )

        tester_agent = Agent(
            name="tester",
            instruction="""You are a QA Engineer. Create comprehensive test suites,
            identify edge cases, and ensure code quality. Write unit tests, integration tests,
            and provide testing strategies.""",
            server_names=["filesystem"] if "filesystem" in context.config.mcp.servers else [],
        )

        reviewer_agent = Agent(
            name="reviewer",
            instruction="""You are a Code Reviewer. Analyze code for quality, security,
            performance, and maintainability. Provide constructive feedback and ensure
            adherence to coding standards and best practices.""",
        )

        # Use parallel execution for development workflow
        parallel_dev = ParallelLLM(
            fan_in_agent=reviewer_agent,
            fan_out_agents=[architect_agent, developer_agent, tester_agent],
            llm_factory=AnthropicAugmentedLLM,
            context=app.context,
        )

        development_prompt = f"""
        Development Task: {task}
        Programming Language: {language}
        Requirements: {requirements}
        
        Architect: Design the system architecture and technical specifications
        Developer: Implement the solution with clean, documented code
        Tester: Create comprehensive tests and quality assurance strategy
        Reviewer: Provide final code review and recommendations
        
        Deliver a complete, production-ready solution.
        """

        result = await parallel_dev.generate_str(message=development_prompt)
        
        logger.info(f"Code development completed for {task}")
        return WorkflowResult(value=result)


@app.workflow
class VIRAOrchestrationWorkflow(Workflow[Dict[str, Any]]):
    """
    Master orchestration workflow that coordinates multiple VIRA agents
    for complex, multi-step projects.
    """

    @app.workflow_run
    async def run(self, project_request: Dict[str, Any]) -> WorkflowResult[str]:
        """
        Orchestrate a complex project using multiple specialized agents.

        Args:
            project_request: Dictionary containing project details

        Returns:
            WorkflowResult containing the coordinated project execution results
        """
        
        project_description = project_request.get('description', 'Complex project')
        project_type = project_request.get('type', 'general')
        priority = project_request.get('priority', 'medium')
        
        logger.info(f"VIRAOrchestrationWorkflow: {project_type} project - {project_description}")
        
        context = app.context
        available_servers = []
        if "filesystem" in context.config.mcp.servers:
            context.config.mcp.servers["filesystem"].args.extend([os.getcwd()])
            available_servers.append("filesystem")
        if "fetch" in context.config.mcp.servers:
            available_servers.append("fetch")

        orchestrator_agent = Agent(
            name="vira_orchestrator",
            instruction="""You are VIRA's Master Orchestrator - the central intelligence that coordinates
            all specialized agents to execute complex projects. Your responsibilities:
            
            1. Project analysis and requirement gathering
            2. Agent selection and task delegation
            3. Workflow coordination and dependency management
            4. Progress monitoring and quality assurance
            5. Integration of results from multiple agents
            6. Final project delivery and documentation
            
            You have access to Planning, Research, and Development agents. Coordinate their efforts
            to deliver exceptional results that exceed user expectations.""",
            server_names=available_servers,
        )

        async with orchestrator_agent:
            logger.info("VIRA Orchestrator: Initializing project coordination...")
            
            llm = await orchestrator_agent.attach_llm(AnthropicAugmentedLLM)
            
            orchestration_result = await llm.generate_str(
                message=f"""Execute this complex project with full agent coordination:
                
                Project: {project_description}
                Type: {project_type}
                Priority: {priority}
                
                As the VIRA Orchestrator, coordinate the execution by:
                1. Breaking down the project into phases
                2. Determining which specialized agents to involve
                3. Managing dependencies between tasks
                4. Ensuring quality and integration
                5. Delivering comprehensive results
                
                Available specialized capabilities:
                - Planning Agent: Task decomposition and execution planning
                - Research Agent: Investigation and analysis
                - Development Team: Architecture, coding, testing, and review
                
                Provide a complete project execution with all phases coordinated.""",
                request_params=RequestParams(
                    modelPreferences=ModelPreferences(
                        intelligencePriority=0.9,
                        costPriority=0.05,
                        speedPriority=0.05,
                    )
                )
            )
            
            logger.info(f"Project orchestration completed: {project_type}")
            return WorkflowResult(value=orchestration_result)


@app.workflow
class ClaudeCodeIntegrationWorkflow(Workflow[Dict[str, str]]):
    """
    Workflow that integrates with Claude Code for repository operations
    and advanced file management.
    """

    @app.workflow_run
    async def run(self, code_request: Dict[str, str]) -> WorkflowResult[str]:
        """
        Execute Claude Code operations for repository management.

        Args:
            code_request: Dictionary with 'operation', 'target', and 'prompt'

        Returns:
            WorkflowResult containing Claude Code execution results
        """
        
        operation = code_request.get('operation', 'analyze')
        target = code_request.get('target', '.')
        prompt = code_request.get('prompt', 'Analyze and improve this code')
        
        logger.info(f"ClaudeCodeIntegrationWorkflow: {operation} on {target}")
        
        context = app.context
        if "filesystem" in context.config.mcp.servers:
            context.config.mcp.servers["filesystem"].args.extend([os.getcwd()])

        claude_code_agent = Agent(
            name="claude_code_specialist",
            instruction="""You are VIRA's Claude Code Integration Specialist. You excel at:
            
            1. Repository analysis and code review
            2. Automated refactoring and optimization
            3. Git workflow management
            4. Project structure improvements
            5. Code generation and documentation
            6. Development workflow automation
            
            You work seamlessly with Claude Code CLI to provide advanced development capabilities
            that go beyond simple code execution to full repository management.""",
            server_names=["filesystem"] if "filesystem" in context.config.mcp.servers else [],
        )

        async with claude_code_agent:
            logger.info("Claude Code Agent: Connected, preparing repository operations...")
            
            llm = await claude_code_agent.attach_llm(AnthropicAugmentedLLM)
            
            integration_result = await llm.generate_str(
                message=f"""Execute Claude Code integration for repository operations:
                
                Operation: {operation}
                Target: {target}
                Prompt: {prompt}
                
                As the Claude Code specialist, provide:
                1. Analysis of the target repository/files
                2. Recommended Claude Code commands
                3. Step-by-step execution plan
                4. Expected outcomes and benefits
                5. Integration with development workflow
                6. Quality assurance and validation steps
                
                Ensure seamless integration between VIRA's intelligence and Claude Code's capabilities.""",
                request_params=RequestParams(
                    modelPreferences=ModelPreferences(
                        intelligencePriority=0.8,
                        speedPriority=0.2,
                        costPriority=0.0,
                    )
                )
            )
            
            logger.info(f"Claude Code integration completed: {operation}")
            return WorkflowResult(value=integration_result)


async def main():
    """Main entry point for VIRA Agent MCP Server"""
    async with app.run() as agent_app:
        # Configure available servers
        context = agent_app.context
        
        # Add filesystem access to current directory
        if "filesystem" in context.config.mcp.servers:
            context.config.mcp.servers["filesystem"].args.extend([os.getcwd()])

        # Log VIRA system initialization
        logger.info("🤖 VIRA Agent System Initializing...")
        logger.info(f"Creating MCP server for {agent_app.name}")

        # Log available workflows (specialized agents)
        logger.info("🎯 Specialized Agent Workflows Available:")
        for workflow_id in agent_app.workflows:
            workflow_descriptions = {
                "PlanningWorkflow": "Task planning and execution coordination",
                "ResearchWorkflow": "Autonomous research and analysis", 
                "CodeDevelopmentWorkflow": "End-to-end software development",
                "VIRAOrchestrationWorkflow": "Multi-agent project coordination",
                "ClaudeCodeIntegrationWorkflow": "Repository management and Claude Code integration"
            }
            description = workflow_descriptions.get(workflow_id, "Specialized workflow")
            logger.info(f"  🔧 {workflow_id}: {description}")

        logger.info("✅ VIRA Agent System Ready - All specialized agents online!")
        
        # Create and run the MCP server
        mcp_server = create_mcp_server_for_app(agent_app)
        await mcp_server.run_stdio_async()


if __name__ == "__main__":
    asyncio.run(main())
