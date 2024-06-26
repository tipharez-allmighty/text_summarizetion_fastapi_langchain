from langchain_huggingface import HuggingFacePipeline


class SimpleSummarizer:
    def __init__(self):
        """
        Initializes the SimpleSummarizer class with a HuggingFacePipeline model for text summarization.

        Using Falconsai/text_summarization because it's fast and provides relatively good results based on feedback
        on the HuggingFace website. It's excellent for testing purposes. Max_length of 50 is set to obtain relatively
        comprehensive summaries in a short period of time. The model inherently supports the summarization task.

        """
        self.llm = HuggingFacePipeline.from_model_id(
            model_id="Falconsai/text_summarization",
            task="summarization",
            pipeline_kwargs={"max_length": 50},
        )

    def summarizer(self, summary_prompt: str) -> str:
        summary = self.llm.invoke(summary_prompt.strip())
        return summary
