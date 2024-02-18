// material-ui
import { Typography } from '@mui/material';

// project imports
import MainCard from 'ui-component/cards/MainCard';

// ==============================|| SAMPLE PAGE ||============================== //

const SamplePage = () => (
  <MainCard title="What should I do with the analysis?">
    <Typography variant="body2">
    You should use the analysis to empower yourself and learn more about your results, but not to diagnose yourself with any medical condition. Proper diagnosis and treatment require a holistic look at your previous medical history, symptoms, lifestyle, and more. Your doctor is the best person to do this.
You can use this information to inspire questions or use it as a starting point for a conversation with your doctor at your next appointment. Asking the right questions can help you know what to expect.

    </Typography>
  </MainCard>
);

export default SamplePage;
