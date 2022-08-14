import gooeypie as gp


class GooeySetProcessor:
    """Offers a UI for performing set operations using Python's
        GooeyPie library."""

    def __init__(self):
        """Initialize GooeyPieApp, create UI elements and run app."""
        self.app = gp.GooeyPieApp("Gooey Set Processor")
        self.app.set_grid(3, 1)
        self.app.width, self.app.height = 600, 800

        # Add Container to group input boxes.
        self.input_container = gp.LabelContainer(self.app, 'Input')
        self.input_container.set_grid(1, 2)

        # Create UI for set entry.
        self.set_a_tbx = gp.Textbox(self.input_container)
        self.input_container.add(self.set_a_tbx, 1, 1, fill=True, stretch=True)

        self.set_b_tbx = gp.Textbox(self.input_container)
        self.input_container.add(self.set_b_tbx, 1, 2, fill=True, stretch=True)

        self.app.add(self.input_container, 1, 1, fill=True, stretch=True)

        # Add Container to group buttons that perform set ops.
        self.ops_container = gp.LabelContainer(self.app, 'Set Operations')
        self.ops_container.set_grid(1, 4)

        # Add button for union operation.
        self.set_union_btn = gp.Button(self.ops_container, '∪ ∙ UNION',
                                       lambda x: self._union(x))
        self.ops_container.add(self.set_union_btn, 1, 1, fill=True, stretch=True)

        # Add button for intersection operation.
        self.set_intersect_btn = gp.Button(self.ops_container, '∩ ∙ INTER',
                                           lambda x: self._intersect(x))
        self.ops_container.add(self.set_intersect_btn, 1, 2, fill=True, stretch=True)

        # Add button for difference of A - B operation.
        self.set_intersect_btn = gp.Button(self.ops_container, 'A - B ∙ DIFF',
                                           lambda x: self._diff_a(x))
        self.ops_container.add(self.set_intersect_btn, 1, 3, fill=True, stretch=True)

        # Add button for difference of B - A operation.
        self.set_intersect_btn = gp.Button(self.ops_container, 'B - A ∙ DIFF',
                                           lambda x: self._diff_b(x))
        self.ops_container.add(self.set_intersect_btn, 1, 4, fill=True, stretch=True)

        self.app.add(self.ops_container, 2, 1, fill=True, stretch=True)

        # Add UI for output.
        self.output_container = gp.LabelContainer(self.app, 'Output')
        self.output_container.set_grid(1, 1)

        self.result_tbx = gp.Textbox(self.output_container)
        self.output_container.add(self.result_tbx, 1, 1, fill=True, stretch=True)

        self.app.add(self.output_container, 3, 1, fill=True, stretch=True)

        self.app.run()

    def _union(self, event):
        """Perform the union of the sets of lines in both textboxes."""
        set_a = set(self.set_a_tbx.text.split('\n'))
        set_b = set(self.set_b_tbx.text.split('\n'))

        result_set = set_a.union(set_b)
        result_txt = '\n'.join(sorted(result_set))

        self.result_tbx.text = result_txt

    def _intersect(self, event):
        set_a = set(self.set_a_tbx.text.split('\n'))
        set_b = set(self.set_b_tbx.text.split('\n'))

        result_set = set_a.intersection(set_b)
        result_txt = '\n'.join(sorted(result_set))

        self.result_tbx.text = result_txt

    def _diff_a(self, event):
        set_a = set(self.set_a_tbx.text.split('\n'))
        set_b = set(self.set_b_tbx.text.split('\n'))

        result_set = set_a.difference(set_b)
        result_txt = '\n'.join(sorted(result_set))

        self.result_tbx.text = result_txt

    def _diff_b(self, event):
        set_a = set(self.set_a_tbx.text.split('\n'))
        set_b = set(self.set_b_tbx.text.split('\n'))

        result_set = set_b.difference(set_a)
        result_txt = '\n'.join(sorted(result_set))

        self.result_tbx.text = result_txt


if __name__ == '__main__':
    gp_app = GooeySetProcessor()
